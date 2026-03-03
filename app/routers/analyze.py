from fastapi import APIRouter, UploadFile, File, Depends
from app.schemas.analysis import AnalysisResponse
from app.models.analysis import Analysis
from app.dependencies import get_current_user
from app.database import get_db
from sqlalchemy.orm import Session
import shutil
import os
import uuid


router = APIRouter()

@router.post("/")
def analyze_image(
    file: UploadFile = File(...), # принимает файл
    current_user = Depends(get_current_user), # доступ к авторизованным юзерам
    db: Session = Depends(get_db) # доступ к бд
):

    UPLOAD_DIR = "uploads"

    os.makedirs(UPLOAD_DIR, exist_ok=True)

    # создание уникального названия файла (защита от перезаписи при дубликации)
    unique_filename = f"{uuid.uuid4()}_{file.filename}"
    file_location = os.path.join(UPLOAD_DIR, unique_filename)

    # создание новой записи в бд
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    new_analysis = Analysis(
        image_path=file_location,
        disease="Mold",
        confidence=0.92,
        recommendation="Use fungicide treatment",
        user_id=current_user.id
    )

    db.add(new_analysis)
    db.commit()

    return {"message": "Uploaded"}