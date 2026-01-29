import React, { useEffect, useState } from "react";
import api from "../services/api";

function Users() {
  const [users, setUsers] = useState([]);
  const [form, setForm] = useState({
    username: "",
    password: "",
    full_name: "",
    status: "active",
    level_id: 1
  });

  const fetchUsers = () => {
    api.get("/users").then(res => setUsers(res.data));
  };

  useEffect(() => {
    fetchUsers();
  }, []);

  const handleChange = (e) => {
    setForm({
      ...form,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    api.post("/users", form).then(() => {
      fetchUsers();
    });
  };

  const deleteUser = (id) => {
    api.delete(`/users/${id}`).then(() => fetchUsers());
  };

  return (
    <div>
      <h2>Users</h2>

      <form onSubmit={handleSubmit}>
        <input name="username" placeholder="Username" onChange={handleChange} />
        <input name="password" placeholder="Password" onChange={handleChange} />
        <input name="full_name" placeholder="Full Name" onChange={handleChange} />
        <button type="submit">Add User</button>
      </form>

      <ul>
        {users.map(user => (
          <li key={user.user_id}>
            {user.username} - {user.full_name}
            <button onClick={() => deleteUser(user.user_id)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Users;
