from pathlib import Path

import pandas as pd

import ast

#Project Paths

#backend/

BASE_DIR = Path(__file__).resolve().parent.parent;

#backend/data/

DATA_DIR = BASE_DIR / "data"

#backend/data/ml_32m/

ML_DATA_DIR = DATA_DIR / "ml-32m"

#TMDB Datasets

MOVIES_FILE = DATA_DIR / "tmdb_5000_movies.csv"

CREDITS_FILE = DATA_DIR / "tmdb_5000_credits.csv"

#MovieLens Datasets

MOVELENS_MOVIES_FILE = ML_DATA_DIR / "movies.csv"

RATINGS_FILE = ML_DATA_DIR / "ratings.csv"

LINKS_FILE = ML_DATA_DIR / "links.csv"

#Output

PREPROCESSED_DATA_DIR = DATA_DIR / "processed_movies.csv"

def parse_json(value):
    try:
        return ast.literal_eval(value)
    except (ValueError, SyntaxError, TypeError):
        return []

def extract_names(value):
    data = parse_json(value)

    if not isinstance(data, list):
        return []

    return [
        item["name"]
        for item in data
        if isinstance(item, dict)
        and "name" in item
    ]


def extract_cast(value, limit=5):
    data = parse_json(value)

    if not isinstance(data, list):
        return []

    return [
        item["name"]
        for item in data[:limit]
        if isinstance(item, dict)
        and "name" in item
    ]


def extract_director(value):
    data = parse_json(value)

    if not isinstance(data, list):
        return ""

    for person in data:
        if (
            isinstance(person, dict)
            and person.get("job") == "Director"
        ):
            return person.get("name", "")

    return ""

def load_datasets():

    movies = pd.read_csv(MOVIES_FILE)

    credits = pd.read_csv(CREDITS_FILE)

    ratings = pd.read_csv(RATINGS_FILE)

    links = pd.read_csv(LINKS_FILE)

    return movies, credits, ratings, links

def preprocess():

    print("Loading datasets...")

    movies, credits, ratings, links = load_datasets()

    print(f"TMDB movies: {len(movies)}")
    print(f"TMDB credits: {len(credits)}")
    print(f"Ratings: {len(ratings)}")
    print(f"MovieLens links: {len(links)}")

    # Rename movie_id so it matches TMDB movie ID
    credits = credits.rename(
        columns={"movie_id": "id"}
    )

    # Merge TMDB movies and credits
    movies = movies.merge(
        credits[["id", "cast", "crew"]],
        on="id",
        how="left"
    )

    # Extract genres
    movies["genres_clean"] = movies["genres"].apply(
        extract_names
    )

    # Extract keywords
    movies["keywords_clean"] = movies["keywords"].apply(
        extract_names
    )

    # Extract top 5 cast members
    movies["cast_clean"] = movies["cast"].apply(
        extract_cast
    )

    # Extract director
    movies["director_clean"] = movies["crew"].apply(
        extract_director
    )

    # Convert lists to strings
    movies["genres_clean"] = movies[
        "genres_clean"
    ].apply(
        lambda x: " ".join(x)
    )

    movies["keywords_clean"] = movies[
        "keywords_clean"
    ].apply(
        lambda x: " ".join(x)
    )

    movies["cast_clean"] = movies[
        "cast_clean"
    ].apply(
        lambda x: " ".join(x)
    )

    # Handle missing overview
    movies["overview"] = movies[
        "overview"
    ].fillna("")

    # Create combined content feature
    movies["combined_features"] = (
        movies["genres_clean"] + " "
        + movies["keywords_clean"] + " "
        + movies["cast_clean"] + " "
        + movies["director_clean"] + " "
        + movies["overview"]
    )

    # Connect TMDB IDs with MovieLens IDs
    movies = movies.merge(
        links[["movieId", "tmdbId"]],
        left_on="id",
        right_on="tmdbId",
        how="left"
    )

    # Save processed dataset
    output_file = PREPROCESSED_DATA_DIR 

    movies.to_csv(
        output_file,
        index=False
    )

    print(
        f"\nProcessed dataset saved to: "
        f"{output_file}"
    )

    print(
        f"Movies with MovieLens IDs: "
        f"{movies['movieId'].notna().sum()}"
    )

    print("\nPreprocessing completed successfully.")

if __name__ == "__main__":
    preprocess()
