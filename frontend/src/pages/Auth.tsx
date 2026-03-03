import { useState, useEffect } from "react";
import { useNavigate, Link } from "react-router-dom";

export default function Auth() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();

  // Проверка токена при загрузке страницы
   useEffect(() => {
       const checkAuth = async () => {
        const token = localStorage.getItem("token");
        if (!token) return;

        const res = await fetch("http://127.0.0.1:8000/auth/protected", {
          headers: {
            Authorization: `Bearer ${token}`
          }
        });

        if (res.ok) {
          navigate("/");
        } else {
          localStorage.removeItem("token");
        }
      };

      checkAuth();
   }, [navigate]);

  const login = async () => {
    const res = await fetch("http://127.0.0.1:8000/auth/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ email, password })
    });

    const data = await res.json();

    if (data.access_token) {
      localStorage.setItem("token", data.access_token);
      navigate("/");
    }

    if (!res.ok) {
      alert("Invalid credentials");
      return;
    }
  };

  return (
    <div>
      <h2>Login</h2>

      <input
        placeholder="Email"
        onChange={e => setEmail(e.target.value)}
      />
      <br />

      <input
        type="password"
        placeholder="Password"
        onChange={e => setPassword(e.target.value)}
      />
      <br />

      <button onClick={login}>Login</button>

      <p>
        Don’t have an account? <Link to="/register">Register</Link>
      </p>
    </div>
  );
}