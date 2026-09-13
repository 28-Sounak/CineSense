from fastapi import APIRouter, HTTPException, Query

from backend.services.recommendation_engine import (
    RecommendationEngine
)


router = APIRouter(
    prefix="/recommendations",
    tags=["Recommendations"]
)


# Create once when the API starts
engine = RecommendationEngine()


@router.get("/search")
def search_movies(
    query: str = Query(
        ...,
        min_length=1
    ),
    limit: int = Query(
        10,
        ge=1,
        le=50
    )
):

    results = engine.search_movies(
        query,
        limit
    )

    return {
        "query": query,
        "count": len(results),
        "results": results
    }


@router.get("/")
def get_recommendations(
    title: str = Query(
        ...,
        min_length=1
    ),
    limit: int = Query(
        10,
        ge=1,
        le=50
    )
):

    results = engine.recommend(
        title,
        limit
    )

    if not results:

        raise HTTPException(
            status_code=404,
            detail=(
                f"Movie '{title}' "
                "was not found."
            )
        )

    return {
        "movie": title,
        "count": len(results),
        "recommendations": results
    }