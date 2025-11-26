from sqlalchemy import Column, Integer, String
from app.core.db import Base

class Plan(Base):
    __tablename__ = "plans"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Integer)
    duration_days = Column(Integer)
