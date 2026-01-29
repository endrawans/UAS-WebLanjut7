import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:5000/api",
  auth: {
    username: "admin",
    password: "admin"
  }
});

export default api;
