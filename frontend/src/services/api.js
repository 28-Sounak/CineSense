const API_BASE_URL = "http://127.0.0.1:8000";

export const SEARCH_LIMIT = 10;
export const RECOMMENDATION_LIMIT = 12;

export async function searchMovies(
  query,
  limit = SEARCH_LIMIT
) {
  const response = await fetch(
    `${API_BASE_URL}/recommendations/search?query=${encodeURIComponent(
      query
    )}&limit=${limit}`
  );

  if (!response.ok) {
    throw new Error("Failed to fetch movies.");
  }

  return response.json();
}

export async function getRecommendations(
  title,
  limit = RECOMMENDATION_LIMIT
) {
  const response = await fetch(
    `${API_BASE_URL}/recommendations/?title=${encodeURIComponent(
      title
    )}&limit=${limit}`
  );

  if (!response.ok) {
    throw new Error("Failed to get recommendations.");
  }

  return response.json();
}

export const API_NAME = "CineSense";
export { API_BASE_URL };