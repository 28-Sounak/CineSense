from pathlib import Path

import pandas as pd


class UserProfileService:

    def __init__(self):

        base_dir = (
            Path(__file__)
            .resolve()
            .parent
            .parent
        )

        ratings_file = (
            base_dir
            / "data"
            / "ml-32m"
            / "ratings.csv"
        )

        self.ratings = pd.read_csv(
            ratings_file,
            usecols=[
                "userId",
                "movieId",
                "rating"
            ]
        )

    def get_user_ratings(
        self,
        user_id: int,
        limit: int = 20
    ):

        user_ratings = self.ratings[
            self.ratings["userId"]
            == user_id
        ]

        user_ratings = user_ratings.sort_values(
            "rating",
            ascending=False
        )

        return user_ratings.head(
            limit
        ).to_dict(
            orient="records"
        )

    def get_average_rating(
        self,
        user_id: int
    ):

        user_ratings = self.ratings[
            self.ratings["userId"]
            == user_id
        ]

        if user_ratings.empty:
            return None

        return round(
            float(
                user_ratings["rating"].mean()
            ),
            2
        )