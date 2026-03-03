import { useEffect, useState } from "react";

export default function History() {
  const [history, setHistory] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/history", {
      headers: {
        Authorization: `Bearer ${localStorage.getItem("token")}`
      }
    })
      .then(res => res.json())
      .then(data => setHistory(data));
  }, []);

  return (
    <div>
      <h1>History</h1>

      {history.map((item: any) => (
        <div key={item.id}>
          <p>{item.disease}</p>
          <p>{item.confidence}</p>
        </div>
      ))}
    </div>
  );
}