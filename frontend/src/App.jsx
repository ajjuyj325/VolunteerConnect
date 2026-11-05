
import { useState, useEffect } from "react";

function App() {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [volunteers, setVolunteers] = useState([]);

  const API = "http://localhost:8000";

  async function loadVolunteers() {
    const response = await fetch(`${API}/volunteers`);
    const data = await response.json();
    setVolunteers(data);
  }

  useEffect(() => {
    loadVolunteers();
  }, []);

  async function registerVolunteer(e) {
    e.preventDefault();

    const response = await fetch(`${API}/volunteers`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ name, email })
    });

    if (!response.ok) {
      alert("Registration failed!");
      return;
    }

    setName("");
    setEmail("");
    await loadVolunteers();
  }

  return (
    <div style={{ padding: "40px", fontFamily: "Arial" }}>
      <h1>VolunteerConnect</h1>
      <p>Register to help your community!</p>

      <form onSubmit={registerVolunteer}>
        <input
          placeholder="Your name"
          value={name}
          onChange={(e) => setName(e.target.value)}
          required
        />

        <input
          type="email"
          placeholder="Your email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />

        <button type="submit">Register</button>
      </form>

      <h2>Registered Volunteers</h2>
      <p>Total Volunteers: {volunteers.length}</p>

      {volunteers.map((volunteer, index) => (
        <p key={index}>
          {volunteer.name} - {volunteer.email}
        </p>
      ))}
    </div>
  );
}

export default App;
