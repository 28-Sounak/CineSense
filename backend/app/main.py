from fastapi import FastAPI

from backend.api.recommendations import (
    router as recommendation_router
)


app = FastAPI(
    title="CineSense API",
    description="Hybrid Movie Recommendation System",
    version="1.0.0"
)


app.include_router(
    recommendation_router
)


@app.get("/")
def root():

    return {
        "message": "CineSense API is running"
    }