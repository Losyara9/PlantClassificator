from fastapi import APIRouter, Depends
from app.schemas.analysis import AnalysisResponse
from app.models.analysis import Analysis
from app.dependencies import get_current_user
from app.database import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/")
def get_history(
    current_user = Depends(get_current_user), # получает текущего юзера и бд
    db: Session = Depends(get_db)
):
    # список анализов конкретного юзера
    return db.query(Analysis).filter(
        Analysis.user_id == current_user.id
    ).all()

@router.get("/{analysis_id}")
def get_history_item(analysis_id: int):
    return AnalysisResponse(
        disease="Mold",
        confidence=0.92,
        recommendation="Use ..."
    )
