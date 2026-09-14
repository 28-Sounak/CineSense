import { useState } from "react";
import {
  searchMovies,
  getRecommendations,
} from "../services/api";

export function useMovies() {
  const [searchResults, setSearchResults] = useState([]);
  const [recommendations, setRecommendations] = useState([]);

  const [selectedMovie, setSelectedMovie] = useState(null);

  const [loadingSearch, setLoadingSearch] = useState(false);
  const [loadingRecommendations, setLoadingRecommendations] =
    useState(false);

  const [error, setError] = useState("");

  const search = async (query) => {
    if (!query.trim()) {
      setSearchResults([]);
      return;
    }

    setLoadingSearch(true);
    setError("");

    try {
      const data = await searchMovies(query);

      setSearchResults(data.results || []);
    } catch (err) {
      console.error(err);
      setError("Unable to search movies.");
    } finally {
      setLoadingSearch(false);
    }
  };

  const recommend = async (movie) => {
    setSelectedMovie(movie);
    setSearchResults([]);
    setRecommendations([]);
    setLoadingRecommendations(true);
    setError("");

    try {
      const data = await getRecommendations(movie.title);

      setRecommendations(data.recommendations || []);
    } catch (err) {
      console.error(err);
      setError("Unable to generate recommendations.");
    } finally {
      setLoadingRecommendations(false);
    }
  };

  const clear = () => {
    setSearchResults([]);
    setRecommendations([]);
    setSelectedMovie(null);
    setError("");
  };

  return {
    searchResults,
    recommendations,
    selectedMovie,

    loadingSearch,
    loadingRecommendations,

    error,

    search,
    recommend,
    clear,
  };
}