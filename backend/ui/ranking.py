import pandas as pd


class HybridRanker:

    def __init__(
        self,
        content_weight: float = 0.6,
        collaborative_weight: float = 0.4
    ):

        self.content_weight = content_weight
        self.collaborative_weight = (
            collaborative_weight
        )

    def rank(
        self,
        content_results,
        collaborative_results,
        limit=10
    ):

        combined = {}

        #Content-based results
        

        for item in content_results:

            movie_id = item.get("movie_id")

            if movie_id is None:
                continue

            combined.setdefault(
                movie_id,
                {
                    "movie_id": movie_id,
                    "tmdb_id": item.get("tmdb_id"),
                    "title": item["title"],
                    "genres": item.get(
                        "genres",
                        ""
                    ),
                    "director": item.get(
                        "director",
                        ""
                    ),
                    "content_score": 0.0,
                    "collaborative_score": 0.0
                }
            )

            combined[movie_id][
                "content_score"
            ] = item.get(
                "similarity",
                0.0
            )

        # Collaborative results

        for item in collaborative_results:

            movie_id = item["movie_id"]

            combined.setdefault(
                movie_id,
                {
                    "movie_id": movie_id,
                    "tmdb_id": item.get("tmdb_id"),
                    "title": item["title"],
                    "genres": "",
                    "director": "",
                    "content_score": 0.0,
                    "collaborative_score": 0.0
                }
            )

            combined[movie_id][
                "collaborative_score"
            ] = item.get(
                "collaborative_score",
                0.0
            )

        # Calculate hybrid score

        results = []

        for movie in combined.values():

            hybrid_score = (
                self.content_weight
                * movie["content_score"]
                +
                self.collaborative_weight
                * movie["collaborative_score"]
            )

            movie["hybrid_score"] = round(
                hybrid_score,
                4
            )

            results.append(movie)

        # Sort

        results.sort(
            key=lambda x: x["hybrid_score"],
            reverse=True
        )

        return results[:limit]