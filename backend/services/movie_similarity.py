from pathlib import Path

import pandas as pd

from backend.ui.content_based import (
    ContentBasedRecommender
)


class MovieSimilarityService:

    def __init__(self):

        base_dir = (
            Path(__file__)
            .resolve()
            .parent
            .parent
        )

        data_file = (
            base_dir
            / "data"
            / "processed_movies.csv"
        )

        self.movies = pd.read_csv(
            data_file
        )

        self.recommender = (
            ContentBasedRecommender(
                self.movies
            )
        )

    def search(
        self,
        query: str,
        limit: int = 10
    ):

        return self.recommender.search_movies(
            query,
            limit
        )

    def similar_movies(
        self,
        title: str,
        limit: int = 10
    ):

        return self.recommender.recommend(
            title,
            limit
        )