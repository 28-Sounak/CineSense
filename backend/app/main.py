from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.api.recommendations import (
    router as recommendation_router
)


app = FastAPI(
    title="CineSense API",
    description="Hybrid Movie Recommendation System",
    version="1.0.0"
)


# Allow the React frontend to communicate with FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(
    recommendation_router
)


@app.get("/")
def root():
    return {
        "message": "CineSense API is running"
    }