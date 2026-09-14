const API_BASE_URL = "http://127.0.0.1:8000";

export async function searchMovies(query, limit = 10)
{
    const response = await fetch(`${API_BASE_URL}/recommendatioons/search?query=${encodeURIComponent(query)}&limit=${limit}`);

    if(!response.ok)
    {
        throw new Error("Failed to fetch movies.");
    }

    return response.json();
}

export async function getRecommendations(title, limit = 12)
{
    const response = await fetch(
    `${API_BASE_URL}/recommendations/?title=${encodeURIComponent(
      title
    )}&limit=${limit}`
  );

  if(!response.ok)
  {
    throw new Error("Failed to get recommendations.");
  }

  return response.json();
}


