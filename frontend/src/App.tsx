import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import Home from "./pages/Home";
import Analyze from "./pages/Analyze";
import History from "./pages/History";
import Diseases from "./pages/Diseases";
import DiseaseDetails from "./pages/DiseaseDetails";
import Auth from "./pages/Auth";
import Register from "./pages/Register";
import ProtectedRoute from "./components/ProtectedRoute";


import { Link } from "react-router-dom";

export default function App() {
  return (
    <BrowserRouter>
    // меню навигации
      <nav>
        <Link to="/">Home</Link> |{" "}
        <Link to="/analyze">Analyze</Link> |{" "}
        <Link to="/history">History</Link> |{" "}
        <Link to="/diseases">Diseases</Link>
      </nav>

      <Routes>
      <Route path="/auth" element={<Auth />} />
      <Route path="/register" element={<Register />} />

      // защищенные маршруты (проверка токена)
      <Route
        path="/"
        element={
          <ProtectedRoute>
            <Home />
          </ProtectedRoute>
        }
      />

      <Route
        path="/history"
        element={
          <ProtectedRoute>
            <History />
          </ProtectedRoute>
        }
      />

      <Route
        path="/diseases"
        element={
          <ProtectedRoute>
            <Diseases />
          </ProtectedRoute>
        }
      />
    </Routes>
    </BrowserRouter>
  );
}


