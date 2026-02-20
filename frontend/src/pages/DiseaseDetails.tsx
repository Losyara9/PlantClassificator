import { useParams } from "react-router-dom";

export default function DiseaseDetails() {
  const { id } = useParams();
  return <h1>Disease Details Page — ID: {id}</h1>;
}
