import axios from "axios";

const api = axios.create({
  baseURL: "http://127.0.0.1:8000",
});

export const searchPapers = async (query) => {
  const response = await api.post("/search", null, {
    params: {
      query: query,
    },
  });

  return response.data;
};

export default api;