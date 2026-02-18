from fastapi import FastAPI
from app.routers import analyze, diseases, history

app = FastAPI(title="Plant Disease Classifier API")

app.include_router(analyze.router, prefix="/analyze", tags=["Analyze"])
app.include_router(diseases.router, prefix="/diseases", tags=["Diseases"])
app.include_router(history.router, prefix="/history", tags=["History"])

@app.get("/")
def root():
    return {"message": "API is running"}
