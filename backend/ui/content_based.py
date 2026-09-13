import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class ContentBasedRecommender:

    def __init__(self, movies_df: pd.DataFrame):

        self.movies = movies_df.reset_index(drop=True)

        self.vectorizer = TfidfVectorizer(
            stop_words="english",
            max_features=15000,
            ngram_range=(1, 2)
        )

        self.tfidf_matrix = self.vectorizer.fit_transform(
            self.movies["combined_features"].fillna("")
        )

        self.movie_indices = pd.Series(
            self.movies.index,
            index=self.movies["title"].str.lower()
        ).drop_duplicates()

    def search_movies(
        self,
        query: str,
        limit: int = 10
    ):

        query = query.strip().lower()

        if not query:
            return []

        matches = self.movies[
            self.movies["title"]
            .str.lower()
            .str.contains(
                query,
                na=False,
                regex=False
            )
        ]

        return matches[
            [
                "id",
                "title",
                "release_date",
                "genres_clean",
                "vote_average",
                "vote_count"
            ]
        ].head(limit).to_dict(
            orient="records"
        )

    def recommend(
        self,
        title: str,
        limit: int = 10
    ):

        title_key = title.strip().lower()

        if title_key not in self.movie_indices:
            return []

        movie_index = self.movie_indices[
            title_key
        ]

        movie_vector = self.tfidf_matrix[
            movie_index
        ]

        similarity_scores = cosine_similarity(
            movie_vector,
            self.tfidf_matrix
        ).flatten()

        similar_indices = (
            similarity_scores
            .argsort()[::-1]
        )

        recommendations = []

        for index in similar_indices:

            if index == movie_index:
                continue

            movie = self.movies.iloc[index]

            recommendations.append({
                "tmdb_id": int(movie["id"]),
                "movie_id": (
                    int(movie["movieId"])
                    if pd.notna(movie["movieId"])
                    else None
                ),
                "title": movie["title"],
                "genres": movie["genres_clean"],
                "director": movie["director_clean"],
                "vote_average": (
                    float(movie["vote_average"])
                    if pd.notna(movie["vote_average"])
                    else 0.0
                ),
                "similarity": round(
                    float(similarity_scores[index]),
                    4
                )
            })

            if len(recommendations) >= limit:
                break

        return recommendations