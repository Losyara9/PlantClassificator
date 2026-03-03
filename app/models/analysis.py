from sqlalchemy import Column, Integer, String, Float, ForeignKey
from app.database import Base

# класс для хранения истории анализа фото юзера
class Analysis(Base):
    __tablename__ = "analyses"

    id = Column(Integer, primary_key=True, index=True)

    image_path = Column(String)
    disease = Column(String)
    confidence = Column(Float)
    recommendation = Column(String)

    user_id = Column(Integer, ForeignKey("users.id"))