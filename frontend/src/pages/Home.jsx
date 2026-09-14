import React from "react";

import Navbar from "../components/Navbar";
import SearchBar from "../components/SearchBar";
import MovieGrid from "../components/MovieGrid";
import Loading from "../components/Loading";
import { useMovies } from "../hooks/useMovies";

function Home() {
  const {
    searchResults,
    recommendations,
    selectedMovie,

    loadingSearch,
    loadingRecommendations,

    error,

    search,
    recommend,
    clear,
  } = useMovies();

  return (
    <div className="app">
      <Navbar />

      <main>
        {/* Hero */}
        <section className="hero" id="home">
          <div className="hero-content">
            <p className="eyebrow">
              AI-POWERED MOVIE DISCOVERY
            </p>

            <h1>
              Find your next
              <span>favorite movie.</span>
            </h1>

            <p className="hero-description">
              CineSense combines content-based filtering and
              collaborative filtering to discover movies
              tailored to your taste.
            </p>

            <SearchBar
              onSearch={search}
              loading={loadingSearch}
            />

            <p className="search-hint">
              Try <strong>Avatar</strong>,{" "}
              <strong>Inception</strong>, or{" "}
              <strong>The Dark Knight</strong>
            </p>
          </div>
        </section>

        {/* Error */}
        {error && (
          <div className="error-message">
            {error}
          </div>
        )}

        {/* Search Results */}
        {searchResults.length > 0 && (
          <section className="section">
            <div className="section-header">
              <div>
                <p className="section-label">
                  SEARCH RESULTS
                </p>

                <h2>Choose a movie</h2>
              </div>

              <button
                className="clear-button"
                onClick={clear}
              >
                Clear
              </button>
            </div>

            <MovieGrid
              movies={searchResults}
              onSelect={recommend}
            />
          </section>
        )}

        {/* Selected Movie */}
        {selectedMovie && (
          <section className="selected-section">
            <div className="selected-movie">
              <div>
                <p className="section-label">
                  SELECTED MOVIE
                </p>

                <h2>{selectedMovie.title}</h2>

                {selectedMovie.genres && (
                  <p className="selected-genres">
                    {selectedMovie.genres}
                  </p>
                )}
              </div>

              <button
                className="change-button"
                onClick={clear}
              >
                Choose another
              </button>
            </div>
          </section>
        )}

        {/* Recommendations */}
        {(loadingRecommendations ||
          recommendations.length > 0) && (
          <section
            className="section"
            id="recommendations"
          >
            <div className="section-header">
              <div>
                <p className="section-label">
                  CINESENSE PICKS
                </p>

                <h2>Recommended for you</h2>
              </div>
            </div>

            {loadingRecommendations ? (
              <Loading message="Analyzing movie similarities..." />
            ) : (
              <MovieGrid
                movies={recommendations}
                recommendations
              />
            )}
          </section>
        )}

        {/* Features */}
        {!selectedMovie &&
          searchResults.length === 0 &&
          recommendations.length === 0 &&
          !loadingSearch && (
            <section className="features-section">
              <div className="feature-card">
                <span className="feature-number">
                  01
                </span>

                <h3>Content-Based</h3>

                <p>
                  Finds movies with similar genres,
                  keywords, cast, directors, and
                  descriptions.
                </p>
              </div>

              <div className="feature-card">
                <span className="feature-number">
                  02
                </span>

                <h3>Collaborative</h3>

                <p>
                  Uses MovieLens rating patterns to
                  identify movies liked by similar
                  audiences.
                </p>
              </div>

              <div className="feature-card">
                <span className="feature-number">
                  03
                </span>

                <h3>Hybrid Ranking</h3>

                <p>
                  Combines both approaches into a
                  single recommendation score.
                </p>
              </div>
            </section>
          )}

        {/* About */}
        <section className="about-section" id="about">
          <p className="section-label">
            ABOUT CINESENSE
          </p>

          <h2>
            Recommendations powered by{" "}
            <span>data and similarity.</span>
          </h2>

          <p>
            CineSense is a hybrid movie recommendation
            system built with Python, FastAPI, React,
            TMDB metadata, and MovieLens ratings.
          </p>

          <div className="tech-stack">
            <span>Python</span>
            <span>FastAPI</span>
            <span>React</span>
            <span>TF-IDF</span>
            <span>Cosine Similarity</span>
            <span>MovieLens</span>
            <span>TMDB</span>
          </div>
        </section>
      </main>

      <footer>
        <p>© 2026 CineSense</p>
        <p>Hybrid Movie Recommendation System</p>
      </footer>
    </div>
  );
}

export default Home;