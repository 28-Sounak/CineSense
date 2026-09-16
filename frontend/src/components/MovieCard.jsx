import React from "react";

function MovieCard({ movie, onSelect, rank }) {
  const score =
    movie.hybrid_score ??
    movie.similarity ??
    movie.collaborative_score ??
    0;

  const percentage =
    Number(score) <= 1
      ? Math.round(Number(score) * 100)
      : Math.round(Number(score));

  return (
    <article className="movie-card">
      <div className="movie-poster">
        <span>
          {rank ? String(rank).padStart(2, "0") : "M"}
        </span>
      </div>

      <div className="movie-card-content">
        {rank && (
          <div className="movie-card-top">
            <span className="match">
              {percentage}% match
            </span>

            {movie.vote_average !== undefined && (
              <span className="rating">
                ★ {Number(movie.vote_average).toFixed(1)}
              </span>
            )}
          </div>
        )}

        <h3>{movie.title}</h3>

        {movie.genres && (
          <p className="genres">{movie.genres}</p>
        )}

        {movie.genres_clean && !movie.genres && (
          <p className="genres">{movie.genres_clean}</p>
        )}

        {movie.director && (
          <p className="director">
            Directed by {movie.director}
          </p>
        )}

        {onSelect && (
          <button
            className="select-movie"
            onClick={() => onSelect(movie)}
          >
            Get recommendations →
          </button>
        )}
      </div>
    </article>
  );
}

export default MovieCard;