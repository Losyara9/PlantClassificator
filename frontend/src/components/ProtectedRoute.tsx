import { Navigate } from "react-router-dom";


export default function ProtectedRoute({ children }: { children: JSX.Element }) {
  const token = localStorage.getItem("token");
    // считывает токен, если его нет то редирект на авторизацию

  if (!token) {
    return <Navigate to="/auth" />;
  }

  return children;
}