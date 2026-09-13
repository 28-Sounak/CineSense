from pathlib import Path

import pandas as pd

from backend.ui.content_based import (
    ContentBasedRecommender
)

from backend.ui.collaborative import (
    CollaborativeRecommender
)

from backend.ui.ranking import (
    HybridRanker
)


class RecommendationEngine:

    def __init__(self):

        base_dir = (
            Path(__file__)
            .resolve()
            .parent
            .parent
        )

        data_dir = base_dir / "data"

        processed_movies_file = (
            data_dir
            / "processed_movies.csv"
        )

        ratings_file = (
            data_dir
            / "ml-32m"
            / "ratings.csv"
        )

        print(
            "Loading processed movie data..."
        )

        self.movies = pd.read_csv(
            processed_movies_file
        )

        print(
            f"Loaded {len(self.movies)} movies."
        )

        print(
            "Loading MovieLens ratings..."
        )

        self.ratings = pd.read_csv(
            ratings_file,
            usecols=[
                "userId",
                "movieId",
                "rating"
            ]
        )

        print(
            f"Loaded {len(self.ratings)} ratings."
        )

        print(
            "Building content-based model..."
        )

        self.content_model = (
            ContentBasedRecommender(
                self.movies
            )
        )

        print(
            "Building collaborative model..."
        )

        self.collaborative_model = (
            CollaborativeRecommender(
                self.ratings,
                self.movies
            )
        )

        self.ranker = HybridRanker(
            content_weight=0.6,
            collaborative_weight=0.4
        )

        print(
            "Recommendation engine ready."
        )

    def search_movies(
        self,
        query: str,
        limit: int = 10
    ):

        return self.content_model.search_movies(
            query,
            limit
        )

    def recommend(
        self,
        title: str,
        limit: int = 10
    ):

        content_results = (
            self.content_model.recommend(
                title,
                limit=50
            )
        )

        if not content_results:
            return []

        # Find the selected movie
        selected = self.movies[
            self.movies["title"]
            .str.lower()
            == title.strip().lower()
        ]

        collaborative_results = []

        if not selected.empty:

            selected_movie = selected.iloc[0]

            movie_id = selected_movie[
                "movieId"
            ]

            if pd.notna(movie_id):

                collaborative_results = (
                    self.collaborative_model
                    .recommend_for_movie(
                        int(movie_id),
                        limit=50
                    )
                )

        return self.ranker.rank(
            content_results,
            collaborative_results,
            limit
        )