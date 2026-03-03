from fastapi import FastAPI
from app.routers import analyze, diseases, history, auth
from app.database import engine, Base
from app import models
from app.models import user
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)


app = FastAPI(title="Plant Disease Classifier API")

# маршрутизаторы
app.include_router(analyze.router, prefix="/analyze", tags=["Analyze"])
app.include_router(diseases.router, prefix="/diseases", tags=["Diseases"])
app.include_router(history.router, prefix="/history", tags=["History"])
app.include_router(auth.router, prefix="/auth")


# разрешенные источники
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# корневой эндпоинт
@app.get("/")
def root():
    return {"message": "API is running"}
