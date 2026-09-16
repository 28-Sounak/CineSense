import pandas as pd

from scipy.sparse import csr_matrix
from sklearn.preprocessing import normalize


class CollaborativeRecommender:

    def __init__(
        self,
        ratings_df: pd.DataFrame,
        movies_df: pd.DataFrame
    ):

        self.ratings = ratings_df[
            [
                "userId",
                "movieId",
                "rating"
            ]
        ].copy()

        self.movies = movies_df.copy()

        # Keep only MovieLens movies that exist
        # in the processed TMDB dataset.
        valid_movie_ids = set(
            self.movies["movieId"]
            .dropna()
            .astype(int)
        )

        self.ratings = self.ratings[
            self.ratings["movieId"].isin(
                valid_movie_ids
            )
        ]

        # Make sure IDs have consistent types.
        self.ratings["userId"] = (
            self.ratings["userId"]
            .astype(int)
        )

        self.ratings["movieId"] = (
            self.ratings["movieId"]
            .astype(int)
        )

        # --------------------------------------------------
        # Create compact integer indices.
        # --------------------------------------------------

        user_codes, self.user_ids = pd.factorize(
            self.ratings["userId"]
        )

        movie_codes, self.movie_ids = pd.factorize(
            self.ratings["movieId"]
        )

        self.user_ids = self.user_ids.to_numpy()
        self.movie_ids = self.movie_ids.to_numpy()

        # --------------------------------------------------
        # Sparse User × Movie matrix
        # --------------------------------------------------

        self.user_movie_matrix = csr_matrix(
            (
                self.ratings["rating"].astype("float32"),
                (
                    user_codes,
                    movie_codes
                )
            ),
            shape=(
                len(self.user_ids),
                len(self.movie_ids)
            ),
            dtype="float32"
        )

        # --------------------------------------------------
        # Normalize movie vectors.
        #
        # Each movie is represented by the users who rated it.
        # --------------------------------------------------

        movie_user_matrix = (
            self.user_movie_matrix.T
        )

        movie_user_matrix = normalize(
            movie_user_matrix,
            axis=1,
            norm="l2"
        )

        # --------------------------------------------------
        # Sparse movie × movie cosine similarity.
        #
        # Only non-zero similarities are stored.
        # --------------------------------------------------

        self.movie_similarity = (
            movie_user_matrix
            @ movie_user_matrix.T
        ).tocsr()

        # --------------------------------------------------
        # Movie lookup table
        # --------------------------------------------------

        self.movie_lookup = (
            self.movies
            .dropna(
                subset=["movieId"]
            )
            .copy()
        )

        self.movie_lookup["movieId"] = (
            self.movie_lookup["movieId"]
            .astype(int)
        )

        self.movie_lookup = (
            self.movie_lookup
            .drop_duplicates(
                subset=["movieId"]
            )
            .set_index("movieId")
        )

        # Movie ID → matrix index
        self.movie_indices = {
            int(movie_id): index
            for index, movie_id
            in enumerate(self.movie_ids)
        }

    def recommend_for_movie(
        self,
        movie_id: int,
        limit: int = 10
    ):

        movie_id = int(movie_id)

        if movie_id not in self.movie_indices:
            return []

        movie_index = self.movie_indices[
            movie_id
        ]

        # Get sparse similarity row.
        row = self.movie_similarity.getrow(
            movie_index
        )

        scores = row.data
        indices = row.indices

        # Sort similarities from highest to lowest.
        ranked_positions = scores.argsort()[::-1]

        recommendations = []

        for position in ranked_positions:

            index = indices[position]

            recommended_movie_id = int(
                self.movie_ids[index]
            )

            # Skip the selected movie itself.
            if recommended_movie_id == movie_id:
                continue

            # Skip movies that don't exist
            # in the metadata table.
            if (
                recommended_movie_id
                not in self.movie_lookup.index
            ):
                continue

            movie = self.movie_lookup.loc[
                recommended_movie_id
            ]

            recommendations.append({
                "movie_id": recommended_movie_id,
                "tmdb_id": int(movie["id"]),
                "title": movie["title"],
                "collaborative_score": round(
                    float(scores[position]),
                    4
                )
            })

            if len(recommendations) >= limit:
                break

        return recommendations