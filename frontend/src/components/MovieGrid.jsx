import MovieCard from "./MovieCard";

function MovieGrid({
  movies,
  onSelect,
  recommendations = false,
}) {
  return (
    <div className="movie-grid">
      {movies.map((movie, index) => (
        <MovieCard
          key={
            movie.movie_id ||
            movie.tmdb_id ||
            movie.id ||
            `${movie.title}-${index}`
          }
          movie={movie}
          onSelect={recommendations ? null : onSelect}
          rank={recommendations ? index + 1 : null}
        />
      ))}
    </div>
  );
}

export default MovieGrid;