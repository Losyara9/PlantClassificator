from pydantic import BaseModel

class AnalysisResponse(BaseModel):
    disease: str
    confidence: float
    recommendation: str