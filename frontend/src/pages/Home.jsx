import { useState } from "react";
import SearchBar from "../components/SearchBar";
import PaperCard from "../components/PaperCard";
import Loading from "../components/Loading";
import { searchPapers } from "../services/api";

function Home() {
  const [papers, setPapers] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleSearch = async (query) => {
    setLoading(true);

    try {
      const data = await searchPapers(query);
      setPapers(data);
    } catch (error) {
      console.error(error);
      alert("Failed to fetch papers.");
    }

    setLoading(false);
  };

  return (
    <div className="container">

      <h1>AI Research Paper Intelligence System</h1>

      <p className="subtitle">
        Search Research Papers using AI Semantic Search
      </p>

      <SearchBar onSearch={handleSearch} />

      {loading && <Loading />}

      {!loading &&
        papers.map((paper, index) => (
          <PaperCard key={index} paper={paper} />
        ))}

    </div>
  );
}

export default Home;