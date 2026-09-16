# CineSense

## Technical Report — Hybrid Movie Recommendation System

**Author:** Sounak Banerjee
**Project:** CineSense
**Type:** Hybrid Movie Recommendation System
**Backend:** Python + FastAPI
**Frontend:** React + Vite
**Recommendation Techniques:** Content-Based Filtering + Collaborative Filtering
**Status:** Functional MVP

---

# Table of Contents

1. [Abstract](#1-abstract)
2. [Introduction](#2-introduction)
3. [Problem Statement](#3-problem-statement)
4. [Objectives](#4-objectives)
5. [Project Scope](#5-project-scope)
6. [System Overview](#6-system-overview)
7. [Technology Stack](#7-technology-stack)
8. [Dataset Description](#8-dataset-description)
9. [Data Processing](#9-data-processing)
10. [Recommendation System](#10-recommendation-system)
11. [Content-Based Filtering](#11-content-based-filtering)
12. [Collaborative Filtering](#12-collaborative-filtering)
13. [Hybrid Recommendation](#13-hybrid-recommendation)
14. [Backend Architecture](#14-backend-architecture)
15. [API Design](#15-api-design)
16. [Frontend Architecture](#16-frontend-architecture)
17. [Frontend Components](#17-frontend-components)
18. [End-to-End Workflow](#18-end-to-end-workflow)
19. [Memory Optimization](#19-memory-optimization)
20. [CORS Configuration](#20-cors-configuration)
21. [Error Handling](#21-error-handling)
22. [Testing](#22-testing)
23. [Example Results](#23-example-results)
24. [Limitations](#24-limitations)
25. [Future Enhancements](#25-future-enhancements)
26. [Project Structure](#26-project-structure)
27. [How to Run](#27-how-to-run)
28. [Conclusion](#28-conclusion)
29. [References](#29-references)

---

# 1. Abstract

CineSense is a hybrid movie recommendation system designed to recommend movies based on both movie characteristics and audience rating patterns.

The system combines two major recommendation approaches:

1. **Content-Based Filtering**, which identifies movies that are similar to a selected movie based on metadata such as genres, keywords, cast, directors, and descriptions.
2. **Collaborative Filtering**, which uses rating patterns from a large collection of MovieLens user ratings to identify relationships between movies based on user preferences.

The outputs of these two approaches are combined into a **hybrid recommendation score**, allowing the system to consider both the characteristics of a movie and patterns observed in user ratings.

The backend is implemented using Python and FastAPI. The frontend is implemented using React and Vite. The system uses TMDB movie metadata and the MovieLens 32M ratings dataset.

A significant implementation challenge was the memory requirement of a dense user-movie matrix during collaborative filtering. The initial implementation attempted to construct a dense matrix with approximately 200,935 users and 4,633 movies, resulting in a memory allocation failure. This was addressed by replacing the dense representation with a sparse matrix implementation using SciPy.

The final system provides a functional search and recommendation interface through a web-based frontend.

---

# 2. Introduction

The rapid growth of digital streaming platforms has resulted in users having access to thousands of movies. While this provides greater choice, it also creates a discovery problem: users may find it difficult to identify movies that match their interests.

A movie recommendation system addresses this problem by analyzing available movie information and/or user interaction data to generate personalized or similarity-based recommendations.

CineSense was developed as a practical implementation of a hybrid recommendation system. Instead of relying exclusively on movie metadata or user ratings, the system combines both approaches.

The system allows a user to search for a movie, select it, and receive a ranked list of recommended movies.

---

# 3. Problem Statement

A traditional movie search system only retrieves movies that match a user's query. It does not necessarily help the user discover movies that they may enjoy.

For example, searching for:

```text
Avatar
```

should not only return the movie *Avatar*. A recommendation system should also identify movies that have relevant characteristics or rating relationships with *Avatar*.

The problem addressed by CineSense is therefore:

> How can a system combine movie metadata and large-scale user rating information to generate relevant movie recommendations while maintaining practical memory and computational requirements?

---

# 4. Objectives

The primary objectives of CineSense are:

* Build a functional movie recommendation system.
* Implement content-based filtering.
* Implement collaborative filtering.
* Combine both approaches into a hybrid model.
* Process a large MovieLens ratings dataset efficiently.
* Provide a REST API for movie search and recommendations.
* Develop a React-based frontend.
* Allow users to search for movies interactively.
* Display ranked recommendations and their scores.
* Maintain a modular backend architecture.

---

# 5. Project Scope

The current version of CineSense focuses on movie search and movie-to-movie recommendations.

## Included

* Movie search
* Movie metadata processing
* Content-based similarity
* Collaborative filtering
* Hybrid scoring
* Recommendation ranking
* REST API
* React frontend
* Loading states
* Error handling
* CORS configuration
* Sparse matrix optimization

## Currently Outside the Scope

The current MVP does not yet implement:

* User authentication
* Persistent user profiles
* Personal watch histories
* Real-time user rating collection
* Production deployment
* Real-time streaming-platform integration
* Advanced deep-learning recommendation models

These can be considered future enhancements.

---

# 6. System Overview

CineSense follows a client-server architecture.

```text
                    ┌──────────────────────┐
                    │      User            │
                    │  Searches for Movie  │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   React Frontend     │
                    │      Vite            │
                    └──────────┬───────────┘
                               │
                         HTTP / JSON
                               │
                               ▼
                    ┌──────────────────────┐
                    │    FastAPI Backend   │
                    └──────────┬───────────┘
                               │
                               ▼
                 ┌──────────────────────────┐
                 │ Recommendation Engine   │
                 └────────────┬─────────────┘
                              │
                ┌─────────────┴─────────────┐
                │                           │
                ▼                           ▼
       ┌─────────────────┐        ┌──────────────────┐
       │ Content-Based   │        │ Collaborative    │
       │ Filtering       │        │ Filtering        │
       └────────┬────────┘        └─────────┬────────┘
                │                           │
                └─────────────┬─────────────┘
                              ▼
                    ┌──────────────────────┐
                    │   Hybrid Ranking     │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Recommended Movies   │
                    └──────────────────────┘
```

---

# 7. Technology Stack

## 7.1 Backend

### Python

Python is used as the primary backend and machine-learning programming language.

Advantages include:

* Extensive data-processing libraries
* Machine-learning ecosystem
* Simple integration with FastAPI
* Pandas and NumPy support

### FastAPI

FastAPI provides the REST API used by the React frontend.

It handles:

* HTTP requests
* Query parameters
* JSON responses
* API routing
* Request validation

### Uvicorn

Uvicorn is used as the ASGI server for running FastAPI.

Example:

```bash
python -m uvicorn backend.app.main:app --reload
```

---

# 7.2 Data and Machine Learning Libraries

The project uses:

* Pandas
* NumPy
* Scikit-learn
* SciPy

Scikit-learn provides functionality related to text vectorization and similarity calculations.

SciPy provides sparse matrix support for collaborative filtering.

---

# 7.3 Frontend

The frontend is implemented using:

* React
* Vite
* JavaScript
* HTML
* CSS

React is responsible for the user interface and application state.

Vite provides the development server and frontend build environment.

---

# 8. Dataset Description

CineSense uses two major sources of data.

## 8.1 TMDB 5000 Dataset

The TMDB 5000 dataset provides movie metadata.

Relevant information includes:

* Movie title
* Movie ID
* Genres
* Keywords
* Cast
* Director
* Overview
* Release information
* Vote statistics

This information is primarily useful for content-based recommendation.

---

# 8.2 MovieLens 32M

The MovieLens 32M dataset provides large-scale user rating information.

The project loaded:

```text
32,000,204 ratings
```

during recommendation-engine initialization.

The rating data contains relationships between:

* Users
* Movies
* Ratings

This information forms the basis of the collaborative filtering component.

---

# 9. Data Processing

Before recommendation generation, the datasets must be loaded and processed.

The backend performs the following general operations:

```text
Load movie data
      ↓
Load MovieLens ratings
      ↓
Filter relevant movie IDs
      ↓
Prepare content features
      ↓
Build content model
      ↓
Build collaborative model
      ↓
Initialize recommendation engine
```

The backend output during successful initialization is:

```text
Loading processed movie data...
Loaded 4806 movies.
Loading MovieLens ratings...
Loaded 32000204 ratings.
Building content-based model...
Building collaborative model...
Recommendation engine ready.
```

This confirms that both recommendation components are initialized before the API begins serving requests.

---

# 10. Recommendation System

CineSense uses a hybrid recommendation architecture.

The recommendation pipeline is:

```text
Selected Movie
      │
      ├───────────────┐
      │               │
      ▼               ▼
Content Model    Collaborative Model
      │               │
      ▼               ▼
Content Score    Collaborative Score
      │               │
      └───────┬───────┘
              ▼
        Hybrid Score
              │
              ▼
       Ranked Movies
```

The objective is to avoid relying exclusively on a single source of information.

---

# 11. Content-Based Filtering

Content-based filtering recommends movies based on similarities between their attributes.

For a selected movie, CineSense can use information such as:

* Genres
* Keywords
* Cast
* Director
* Description

These fields are converted into textual features.

---

## 11.1 TF-IDF

TF-IDF stands for **Term Frequency–Inverse Document Frequency**.

It represents text based on the importance of individual terms.

The general TF-IDF concept is:

```text
TF-IDF(term, document)
=
TF(term, document)
×
IDF(term)
```

Terms that are common across many movies receive lower importance, while terms that are more distinctive receive higher importance.

---

## 11.2 Cosine Similarity

After converting movie metadata into vectors, cosine similarity can be used to compare movies.

Cosine similarity measures the angle between two vectors.

Conceptually:

```text
             A · B
Similarity = ───────
             |A||B|
```

A larger similarity indicates that the feature vectors point in more similar directions.

---

## 11.3 Content Score

The content model produces a similarity score for candidate movies.

For example:

```text
Avatar → Interstellar
Content Score = 0.1419
```

This score represents the content-based similarity calculated by the recommendation system.

---

# 12. Collaborative Filtering

Collaborative filtering uses user-rating behavior rather than only movie metadata.

The basic assumption is that movies receiving similar rating patterns from users may have a relationship.

For example:

```text
Users
 │
 ├── Movie A → 4.5
 ├── Movie B → 4.0
 ├── Movie C → 2.0
 │
 └── ...
```

When many users exhibit similar relationships between movies, the system can use those patterns to generate recommendations.

---

# 13. Hybrid Recommendation

The key feature of CineSense is the combination of content-based and collaborative filtering.

Each candidate movie receives:

* Content score
* Collaborative score
* Hybrid score

An example output is:

```json
{
  "title": "Interstellar",
  "content_score": 0.1419,
  "collaborative_score": 0.5112,
  "hybrid_score": 0.2896
}
```

The hybrid score is calculated by combining the two component scores according to the implementation's weighting.

Conceptually:

```text
Hybrid Score
      =
Content contribution
      +
Collaborative contribution
```

The exact weighting is determined by the recommendation engine implementation.

This approach allows CineSense to incorporate two different forms of evidence:

1. Similarity between movie characteristics.
2. Similarity derived from user-rating behavior.

---

# 14. Backend Architecture

The backend is organized into several layers.

```text
backend/
│
├── api/
│   └── recommendations.py
│
├── app/
│   └── main.py
│
├── services/
│   └── recommendation_engine.py
│
└── ui/
    └── collaborative.py
```

---

## 14.1 `main.py`

`main.py` creates the FastAPI application.

It:

* Initializes FastAPI.
* Configures CORS.
* Registers API routers.
* Provides the root endpoint.

---

## 14.2 `recommendations.py`

This module defines recommendation-related API endpoints.

The router uses:

```text
/recommendations
```

as its prefix.

It provides:

```text
/recommendations/search
/recommendations/
```

---

## 14.3 `recommendation_engine.py`

This is the central recommendation component.

It coordinates:

* Movie data
* Content-based recommendations
* Collaborative recommendations
* Hybrid ranking

The recommendation engine is initialized when the backend starts.

---

## 14.4 `collaborative.py`

This module implements collaborative filtering.

A major optimization was introduced here to avoid constructing a very large dense user-movie matrix.

The final implementation uses:

```text
SciPy CSR sparse matrix
```

for rating data.

---

# 15. API Design

## 15.1 Root Endpoint

```http
GET /
```

Response:

```json
{
  "message": "CineSense API is running"
}
```

---

## 15.2 Search Endpoint

```http
GET /recommendations/search
```

Parameters:

| Parameter | Description               | Example  |
| --------- | ------------------------- | -------- |
| `query`   | Movie search text         | `Avatar` |
| `limit`   | Maximum number of results | `10`     |

Example:

```text
/recommendations/search?query=Avatar&limit=10
```

Example response:

```json
{
  "query": "Avatar",
  "count": 1,
  "results": [
    {
      "id": 19995,
      "title": "Avatar",
      "release_date": "2009-12-10",
      "genres_clean": "Action Adventure Fantasy Science Fiction",
      "vote_average": 7.2,
      "vote_count": 11800
    }
  ]
}
```

---

## 15.3 Recommendation Endpoint

```http
GET /recommendations/
```

Parameters:

| Parameter | Description               | Example  |
| --------- | ------------------------- | -------- |
| `title`   | Selected movie title      | `Avatar` |
| `limit`   | Number of recommendations | `12`     |

Example:

```text
/recommendations/?title=Avatar&limit=12
```

The response contains:

* Movie ID
* TMDB ID
* Title
* Genres
* Director
* Content score
* Collaborative score
* Hybrid score

---

# 16. Frontend Architecture

The frontend is organized using reusable React components.

```text
frontend/src/
│
├── components/
│   ├── Loading.jsx
│   ├── MovieCard.jsx
│   ├── MovieGrid.jsx
│   ├── Navbar.jsx
│   └── SearchBar.jsx
│
├── hooks/
│   └── useMovies.js
│
├── pages/
│   └── Home.jsx
│
├── services/
│   └── api.js
│
├── data/
│   └── config.js
│
├── App.jsx
├── Main.jsx
└── index.css
```

---

# 17. Frontend Components

## 17.1 `App.jsx`

`App.jsx` is the main application component.

It renders:

```text
Home
```

---

## 17.2 `Home.jsx`

`Home.jsx` controls the main application interface.

It contains:

* Navigation
* Hero section
* Search bar
* Search results
* Selected movie
* Recommendations
* Feature information
* About section
* Footer

It also consumes the `useMovies` hook.

---

## 17.3 `SearchBar.jsx`

The search component manages the search input.

The process is:

```text
User enters query
       ↓
Form submitted
       ↓
Query validated
       ↓
search()
       ↓
Backend API
```

---

## 17.4 `MovieGrid.jsx`

`MovieGrid` displays multiple movie cards.

It receives:

* Movie list
* Selection handler
* Recommendation state

and maps each movie into a `MovieCard`.

---

## 17.5 `MovieCard.jsx`

`MovieCard` displays information about an individual movie.

Depending on the context, it can show:

* Movie title
* Genres
* Director
* Match percentage
* Rating
* Recommendation rank
* Recommendation button

---

## 17.6 `Loading.jsx`

This component displays a loading state while an API request is being processed.

Examples include:

```text
Searching...
```

and:

```text
Analyzing movie similarities...
```

---

## 17.7 `useMovies.js`

The `useMovies` custom React hook manages application state.

Important state variables include:

```text
searchResults
recommendations
selectedMovie
loadingSearch
loadingRecommendations
error
```

It provides functions such as:

```text
search()
recommend()
clear()
```

---

## 17.8 `api.js`

This module contains frontend API communication.

The backend base URL is:

```text
http://127.0.0.1:8000
```

The frontend uses `fetch()` to communicate with FastAPI.

---

# 18. End-to-End Workflow

The complete user interaction is:

## Step 1 — Search

The user enters:

```text
Avatar
```

and clicks Search.

---

## Step 2 — Frontend Request

React calls:

```text
GET /recommendations/search?query=Avatar&limit=10
```

---

## Step 3 — Backend Search

FastAPI receives the request and searches the available movie data.

---

## Step 4 — Search Result

The backend returns the matching movie.

```text
Avatar
2009
Action / Adventure / Fantasy / Science Fiction
```

---

## Step 5 — Movie Selection

The user selects Avatar.

React sends:

```text
GET /recommendations/?title=Avatar&limit=12
```

---

## Step 6 — Recommendation Engine

The recommendation engine processes Avatar using:

```text
Content-Based Filtering
+
Collaborative Filtering
```

---

## Step 7 — Hybrid Ranking

Candidate movies are assigned hybrid scores and ranked.

---

## Step 8 — Frontend Display

React displays the recommendations as movie cards.

---

# 19. Memory Optimization

One of the most important engineering issues encountered during development involved the collaborative filtering implementation.

## 19.1 Initial Approach

The initial implementation created a user-movie matrix using Pandas:

```python
ratings.pivot_table(
    index="userId",
    columns="movieId",
    values="rating",
    aggfunc="mean"
).fillna(0)
```

This created a dense representation.

After filtering, the approximate dimensions were:

```text
200,935 users
×
4,633 movies
```

This results in approximately:

```text
20.09 × 10^9
```

potential matrix elements.

Because missing ratings were replaced with zero, a large dense floating-point array was required.

The application consequently failed with a memory allocation error of approximately:

```text
6.94 GiB
```

---

## 19.2 Problem

Most users have rated only a small subset of the available movies.

Therefore, most cells of the user-movie matrix are zero.

A dense matrix stores all of those zeros explicitly, which is inefficient.

---

## 19.3 Sparse Matrix Solution

The implementation was changed to use:

```python
scipy.sparse.csr_matrix
```

CSR stands for:

> Compressed Sparse Row

Instead of storing every zero, the sparse matrix primarily stores non-zero rating values and their locations.

This dramatically reduces the memory required for sparse rating data.

---

## 19.4 Result

After implementing the sparse representation, the backend successfully initialized:

```text
Loading processed movie data...
Loaded 4806 movies.
Loading MovieLens ratings...
Loaded 32000204 ratings.
Building content-based model...
Building collaborative model...
Recommendation engine ready.
```

This confirmed that the collaborative filtering component could be initialized without the previous dense-matrix memory failure.

---

# 20. CORS Configuration

During frontend integration, the browser initially rejected API requests because the frontend and backend were running on different origins.

Frontend:

```text
http://localhost:5173
```

Backend:

```text
http://127.0.0.1:8000
```

The browser therefore produced a CORS error.

FastAPI was configured with `CORSMiddleware` to allow the React development server.

Allowed origins include:

```text
http://localhost:5173
http://127.0.0.1:5173
```

This allows the frontend to make API requests to the FastAPI backend during development.

---

# 21. Error Handling

The application includes error handling at both the backend and frontend levels.

## Backend

FastAPI validates query parameters.

For example:

```text
query
minimum length = 1
```

and:

```text
limit
minimum = 1
maximum = 50
```

If a requested movie cannot be found for recommendations, the API can return an HTTP 404 response.

---

## Frontend

The React application tracks an `error` state.

If a search fails:

```text
Unable to search movies.
```

If recommendation generation fails:

```text
Unable to generate recommendations.
```

Loading states prevent the user from repeatedly submitting the same request while a request is in progress.

---

# 22. Testing

Testing was performed at multiple levels.

## 22.1 Backend Startup Test

The backend successfully initializes with:

```bash
python -m uvicorn backend.app.main:app --reload
```

Expected output:

```text
Recommendation engine ready.
Application startup complete.
```

---

## 22.2 API Search Test

Request:

```text
/recommendations/search?query=Avatar&limit=10
```

Result:

```text
HTTP 200 OK
```

---

## 22.3 Recommendation Test

Request:

```text
/recommendations/?title=Avatar&limit=12
```

Result:

```text
HTTP 200 OK
```

with 12 recommendation objects.

---

## 22.4 Frontend Integration Test

The following workflow was successfully tested:

```text
Enter movie
    ↓
Click Search
    ↓
Search result displayed
    ↓
Select movie
    ↓
Generate recommendations
    ↓
Recommendations displayed
```

---

# 23. Example Results

The following example was generated using:

```text
Avatar
```

The recommendation system returned 12 movies.

| Rank | Movie                   | Content Score | Collaborative Score | Hybrid Score |
| ---: | ----------------------- | ------------: | ------------------: | -----------: |
|    1 | Interstellar            |        0.1419 |              0.5112 |       0.2896 |
|    2 | Gravity                 |        0.1597 |              0.4602 |       0.2799 |
|    3 | Guardians of the Galaxy |        0.1388 |              0.4913 |       0.2798 |
|    4 | Star Trek               |        0.1286 |              0.4914 |       0.2737 |
|    5 | Iron Man                |        0.0000 |              0.5888 |       0.2355 |
|    6 | Inception               |        0.0000 |              0.5829 |       0.2332 |
|    7 | WALL·E                  |        0.0000 |              0.5598 |       0.2239 |
|    8 | Up                      |        0.0000 |              0.5529 |       0.2212 |
|    9 | The Dark Knight         |        0.0000 |              0.5430 |       0.2172 |
|   10 | District 9              |        0.0000 |              0.5335 |       0.2134 |
|   11 | The Avengers            |        0.0000 |              0.5189 |       0.2076 |
|   12 | Inglourious Basterds    |        0.0000 |              0.5088 |       0.2035 |

These values demonstrate that the recommendation engine is returning separate scores from the content-based and collaborative components and combining them into a hybrid score.

---

# 24. Limitations

The current implementation has several limitations.

## 24.1 Cold-Start Problem

Collaborative filtering depends on historical rating data.

Movies with limited rating information may not receive strong collaborative signals.

---

## 24.2 Metadata Availability

Some recommended movies may not contain complete metadata in the currently joined datasets.

For example, some results may have empty:

```text
genres
director
```

fields.

This affects presentation and may also reduce the contribution of content-based features.

---

## 24.3 Movie-Level Rather Than User-Level Personalization

The current interface primarily recommends movies based on a selected movie.

It does not yet maintain a persistent user profile containing:

* Previously watched movies
* Personal ratings
* Favorite genres
* Individual recommendation history

Therefore, the current system should be considered a movie-to-movie recommendation engine rather than a fully personalized user recommendation platform.

---

## 24.4 Dataset Limitations

The recommendation quality is dependent on the available datasets.

The datasets may not contain every currently released movie and may not reflect current audience preferences.

---

## 24.5 Computational Requirements

Although sparse matrices significantly reduce memory consumption, building recommendation models from tens of millions of ratings remains computationally intensive.

The recommendation engine is therefore initialized when the backend starts rather than rebuilding the entire model for every API request.

---

# 25. Future Enhancements

Several improvements can be implemented in future versions.

## 25.1 Personalized User Profiles

Users could create accounts and maintain:

* Favorite movies
* Ratings
* Watch history
* Preferred genres

The recommendation engine could then generate personalized recommendations.

---

## 25.2 Improved Collaborative Filtering

The current collaborative implementation can be further optimized using top-K nearest-neighbor methods rather than calculating unnecessary movie-pair similarities.

This could improve scalability for larger datasets.

---

## 25.3 Movie Posters

Movie poster images can be retrieved using TMDB identifiers and displayed in the React interface.

This would make the recommendation interface more visually informative.

---

## 25.4 Recommendation Explanations

The system could explain recommendations using messages such as:

```text
Recommended because you selected a Science Fiction movie.
```

or:

```text
Users who rated this movie highly also rated this movie highly.
```

Such explanations would make the recommendation process easier to understand.

---

## 25.5 User Rating System

The frontend could allow users to rate recommended movies.

These ratings could eventually be incorporated into a user-specific recommendation model.

---

## 25.6 Evaluation Metrics

Future versions should formally evaluate recommendation quality using metrics such as:

* Precision@K
* Recall@K
* F1-score
* Mean Average Precision
* NDCG
* RMSE for rating prediction, where appropriate

Offline evaluation would allow the recommendation algorithms and hybrid weights to be compared objectively.

---

## 25.7 Deployment

The system can eventually be deployed using:

* Cloud-hosted FastAPI backend
* Production React build
* Managed database or data storage
* Containerization using Docker
* Cloud infrastructure

---

# 26. Project Structure

The primary project structure is:

```text
CineSense/
│
├── backend/
│   ├── api/
│   │   ├── auth.py
│   │   ├── movies.py
│   │   ├── ratings.py
│   │   ├── recommendations.py
│   │   └── users.py
│   │
│   ├── app/
│   │   └── main.py
│   │
│   ├── services/
│   │   └── recommendation_engine.py
│   │
│   └── ui/
│       └── collaborative.py
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── data/
│   │   ├── hooks/
│   │   ├── pages/
│   │   └── services/
│   │
│   └── package.json
│
├── data/
│   ├── tmdb_5000_credits.csv
│   ├── tmdb_5000_movies.csv
│   └── ml-32m/
│
├── requirements.txt
├── README.md
└── TECHNICAL_REPORT.md
```

---

# 27. How to Run

## Backend

From the project root:

```powershell
cd "C:\Users\SOUNAK BANERJEE\CineSense"
```

Start FastAPI:

```powershell
python -m uvicorn backend.app.main:app --reload
```

The backend runs at:

```text
http://127.0.0.1:8000
```

---

## Frontend

Open another PowerShell terminal:

```powershell
cd "C:\Users\SOUNAK BANERJEE\CineSense\frontend"
```

Install dependencies if necessary:

```powershell
npm install
```

Start Vite:

```powershell
npm run dev
```

The frontend normally runs at:

```text
http://localhost:5173
```

---

## Usage

1. Start the FastAPI backend.
2. Start the React frontend.
3. Open the frontend in a browser.
4. Enter a movie title.
5. Click **Search**.
6. Select a movie.
7. Click **Get recommendations**.
8. View the generated hybrid recommendations.

---

# 28. Conclusion

CineSense demonstrates the implementation of a hybrid movie recommendation system combining content-based and collaborative filtering.

The project integrates:

```text
Movie Metadata
      +
Large-Scale User Ratings
      ↓
Recommendation Models
      ↓
Hybrid Scoring
      ↓
Ranked Recommendations
      ↓
FastAPI
      ↓
React Frontend
```

A major engineering challenge involved processing the large MovieLens dataset without exhausting system memory. The initial dense user-movie representation required several gigabytes of memory and caused backend initialization to fail. Replacing the dense representation with a sparse CSR matrix allowed the collaborative filtering component to initialize successfully.

The final MVP successfully supports movie search and hybrid movie recommendations through a web interface.

The project also provides a foundation for future improvements including personalized user profiles, stronger collaborative filtering algorithms, recommendation evaluation, movie posters, recommendation explanations, and production deployment.

CineSense therefore serves as both a practical recommendation-system implementation and a foundation for further experimentation with information retrieval, machine learning, data processing, and full-stack application development.

---

# 29. References

1. **MovieLens Dataset**
   GroupLens Research, University of Minnesota.

2. **TMDB 5000 Movie Dataset**
   The Movie Database (TMDB) metadata.

3. **Scikit-learn Documentation**
   Machine learning and text-processing utilities.

4. **SciPy Documentation**
   Sparse matrix and scientific computing utilities.

5. **FastAPI Documentation**
   Python framework for building APIs.

6. **React Documentation**
   React library for building user interfaces.

7. **Vite Documentation**
   Frontend development and build tooling.

---

## Project Summary

```text
Project Name       : CineSense
Project Type       : Hybrid Movie Recommendation System
Backend            : Python + FastAPI
Frontend           : React + Vite
Content Filtering  : TF-IDF + Cosine Similarity
Collaborative      : MovieLens Rating-Based Filtering
Optimization       : Sparse CSR Matrix
API                : REST
Current Status     : Functional MVP
```

**Author:** Sounak Banerjee
