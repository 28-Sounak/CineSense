import pandas as pd

from sklearn.metrics.pairwise import cosine_similarity


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

        # User × Movie matrix
        self.user_movie_matrix = (
            self.ratings
            .pivot_table(
                index="userId",
                columns="movieId",
                values="rating",
                aggfunc="mean"
            )
            .fillna(0)
        )

        self.movie_ids = (
            self.user_movie_matrix.columns
            .to_numpy()
        )

        self.movie_indices = {
            movie_id: index
            for index, movie_id
            in enumerate(self.movie_ids)
        }

        # Movie × Movie similarity
        self.movie_similarity = cosine_similarity(
            self.user_movie_matrix.T
        )

        self.movie_lookup = (
            self.movies
            .dropna(subset=["movieId"])
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

        scores = self.movie_similarity[
            movie_index
        ]

        ranked_indices = (
            scores
            .argsort()[::-1]
        )

        recommendations = []

        for index in ranked_indices:

            recommended_movie_id = int(
                self.movie_ids[index]
            )

            if recommended_movie_id == movie_id:
                continue

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
                    float(scores[index]),
                    4
                )
            })

            if len(recommendations) >= limit:
                break

        return recommendations