import {useState} from "react";

function searchBar({onSearch, loading})
{
    const [query, setQuery] = useState("");

    const handleSubmit = (event) => {
        event.preventDefault();

        if(!query.trim())
        {
            return;
        }

        onSearch(query);
    };

    return
    {
        <form className = "search-container" onSubnit = {handleSubmit}>
            <input 
            type = "text"

            placeholder = "Search for a movie..."

            value = {query}

            onChange = {(event) => setQuery(event.target.value)}
            />

            <button type = "submit" disabled = {loading}>
                {loading ? "Searching..." : "Search"}
            </button>
        </form>
    };
}

export default searchBar;