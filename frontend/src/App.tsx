import { BrowserRouter, Routes, Route } from "react-router-dom";
import Home from "./pages/Home";
import Analyze from "./pages/Analyze";
import History from "./pages/History";
import Diseases from "./pages/Diseases";
import DiseaseDetails from "./pages/DiseaseDetails";

import { Link } from "react-router-dom";

export default function App() {
  return (
    <BrowserRouter>
      <nav>
        <Link to="/">Home</Link> |{" "}
        <Link to="/analyze">Analyze</Link> |{" "}
        <Link to="/history">History</Link> |{" "}
        <Link to="/diseases">Diseases</Link>
      </nav>

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/analyze" element={<Analyze />} />
        <Route path="/history" element={<History />} />
        <Route path="/diseases" element={<Diseases />} />
        <Route path="/diseases/:id" element={<DiseaseDetails />} />
      </Routes>
    </BrowserRouter>
  );
}


