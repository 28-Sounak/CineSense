# CineSense

### Hybrid Movie Recommendation System

CineSense is a movie recommendation system that combines **content-based filtering** and **collaborative filtering** to recommend movies based on movie characteristics and audience rating patterns.

The project uses **Python and FastAPI** for the recommendation backend and **React + Vite** for the frontend.

---

## Features

* Search for movies by title
* Content-based movie recommendations
* Collaborative filtering using MovieLens ratings
* Hybrid recommendation scoring
* Movie similarity based on metadata
* FastAPI REST API
* React-based interactive frontend
* Search and recommendation loading states
* Responsive movie recommendation interface

---

## How It Works

CineSense uses two recommendation approaches:

### 1. Content-Based Filtering

The content-based model compares movie information such as:

* Genres
* Keywords
* Cast
* Directors
* Movie descriptions

Text features are processed using **TF-IDF**, and movie similarity is calculated using **cosine similarity**.

### 2. Collaborative Filtering

The collaborative filtering model uses rating patterns from the **MovieLens dataset**.

Instead of creating a large dense user-movie matrix, CineSense uses a **sparse matrix representation** to handle the large MovieLens dataset more efficiently.

### 3. Hybrid Recommendation

The results from both approaches are combined into a hybrid score.

Conceptually:

```text
Content-Based Score
        +
Collaborative Score
        ↓
   Hybrid Score
        ↓
Recommended Movies
```

This allows CineSense to consider both **movie similarity** and **audience rating patterns**.

---

## Tech Stack

### Backend

* Python
* FastAPI
* Pandas
* NumPy
* Scikit-learn
* SciPy
* Uvicorn

### Frontend

* React
* Vite
* JavaScript
* HTML
* CSS

### Machine Learning / Recommendation

* TF-IDF
* Cosine Similarity
* Sparse Matrix Representation
* Collaborative Filtering
* Hybrid Recommendation

### Datasets

* TMDB 5000 Movie Dataset
* MovieLens 32M Dataset

---

## Project Structure

```text
CineSense/
│
├── backend/
│   │
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
├── data/
│   ├── tmdb_5000_credits.csv
│   ├── tmdb_5000_movies.csv
│   └── ml-32m/
│       ├── links.csv
│       ├── movies.csv
│       ├── ratings.csv
│       └── README.txt
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── Loading.jsx
│   │   │   ├── MovieCard.jsx
│   │   │   ├── MovieGrid.jsx
│   │   │   ├── Navbar.jsx
│   │   │   └── SearchBar.jsx
│   │   │
│   │   ├── data/
│   │   │   └── config.js
│   │   │
│   │   ├── hooks/
│   │   │   └── useMovies.js
│   │   │
│   │   ├── pages/
│   │   │   └── Home.jsx
│   │   │
│   │   ├── services/
│   │   │   └── api.js
│   │   │
│   │   ├── App.jsx
│   │   ├── Main.jsx
│   │   └── index.css
│   │
│   └── package.json
│
├── requirements.txt
└── README.md
```

> The exact data-folder location can vary depending on your local project setup.

---

## Backend Setup

### 1. Clone the repository

```bash
git clone https://github.com/28-Sounak/CineSense.git
cd CineSense
```

### 2. Install Python dependencies

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
venv\Scripts\activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

### 3. Start the FastAPI server

From the project root:

```powershell
python -m uvicorn backend.app.main:app --reload
```

The backend will run at:

```text
http://127.0.0.1:8000
```

---

## Frontend Setup

Open another terminal:

```powershell
cd frontend
```

Install the Node dependencies:

```powershell
npm install
```

Start the development server:

```powershell
npm run dev
```

The frontend will normally be available at:

```text
http://localhost:5173
```

---

## API Endpoints

### API Status

```http
GET /
```

Example response:

```json
{
  "message": "CineSense API is running"
}
```

### Search Movies

```http
GET /recommendations/search?query=Avatar&limit=10
```

Example:

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

### Get Recommendations

```http
GET /recommendations/?title=Avatar&limit=12
```

Example recommendation fields include:

```json
{
  "title": "Interstellar",
  "content_score": 0.1419,
  "collaborative_score": 0.5112,
  "hybrid_score": 0.2896
}
```

---

## Recommendation Pipeline

```text
                  Movie Search
                       │
                       ▼
                Search Database
                       │
                       ▼
                Select a Movie
                       │
             ┌─────────┴─────────┐
             │                   │
             ▼                   ▼
      Content-Based       Collaborative
         Filtering           Filtering
             │                   │
             │                   │
             └─────────┬─────────┘
                       ▼
                Hybrid Scoring
                       │
                       ▼
                Ranked Results
                       │
                       ▼
                 React Frontend
```

---

## Example

Searching for:

```text
Avatar
```

can produce recommendations such as:

* Interstellar
* Gravity
* Guardians of the Galaxy
* Star Trek
* Iron Man
* Inception
* WALL·E
* Up
* The Dark Knight
* District 9
* The Avengers
* Inglourious Basterds

The exact recommendations and scores depend on the underlying datasets and recommendation model.

---

## Performance Consideration

The MovieLens 32M dataset contains more than **32 million ratings**.

A dense user-movie matrix would require substantial memory. CineSense therefore uses **SciPy sparse matrices** for the collaborative filtering component to avoid allocating a very large dense matrix.

This makes the recommendation engine substantially more memory-efficient than a straightforward dense-matrix implementation.

---

## Frontend

The React frontend provides:

* Movie search
* Search results
* Movie selection
* Recommendation generation
* Recommendation cards
* Match scores
* Movie genres and director information
* Loading indicators
* Error handling

The frontend communicates with the FastAPI backend through REST API requests.

---

## Future Improvements

Potential improvements include:

* Movie poster integration
* More complete movie metadata
* User accounts and personalized profiles
* User rating functionality
* Watch history
* "Because you watched..." recommendations
* Improved collaborative filtering using top-K nearest neighbors
* Recommendation explanations
* Better cold-start handling
* Advanced hybrid weighting
* Recommendation evaluation using metrics such as Precision@K and Recall@K
* Deployment of the frontend and backend
* Improved mobile responsiveness

---

## Project Status

**Current Status: Functional MVP**

The core recommendation pipeline is implemented and connected to the React frontend.

```text
Search              ✓
Content Filtering   ✓
Collaborative       ✓
Hybrid Ranking      ✓
FastAPI Backend     ✓
React Frontend      ✓
API Integration     ✓
```

---

## Author

**Sounak Banerjee**

B.Tech Computer Science & Engineering

---

## License

This project is intended for educational and portfolio purposes.
