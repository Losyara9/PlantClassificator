from fastapi import APIRouter
from app.schemas.disease import Disease

router = APIRouter()

@router.get("/")
def get_diseases():
    return [
        Disease(id=1, name="Mold"),
        Disease(id=2, name="Powdery Mildew")
    ]

@router.get("/{disease_id}")
def get_disease(disease_id: int):
    return Disease(id=disease_id, name="Mold")