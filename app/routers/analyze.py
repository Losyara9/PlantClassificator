from fastapi import APIRouter
from app.schemas.analysis import AnalysisResponse

router = APIRouter()

@router.post("/")
def analyze_image():
    return AnalysisResponse(
        disease="Mold",
        confidence=0.92,
        recommendation="Use ..."
    )