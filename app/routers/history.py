from fastapi import APIRouter
from app.schemas.analysis import AnalysisResponse

router = APIRouter()

@router.get("/")
def get_history():
    return [
        AnalysisResponse(
            disease="Mold",
            confidence=0.92,
            recommendation="Use ..."
        ),
        AnalysisResponse(
            disease="Powdery Mildew",
            confidence=0.85,
            recommendation="Remove affected leaves."
        )
    ]


@router.get("/{analysis_id}")
def get_history_item(analysis_id: int):
    return AnalysisResponse(
        disease="Mold",
        confidence=0.92,
        recommendation="Use ..."
    )
