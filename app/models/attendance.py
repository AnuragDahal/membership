from sqlalchemy import Column, Integer, ForeignKey, DateTime
from app.core.db import Base
from datetime import datetime

class Attendance(Base):
    __tablename__ = "attendance"
    id = Column(Integer, primary_key=True, index=True)
    member_id = Column(Integer, ForeignKey("members.id"), index=True)
    check_in = Column(DateTime, default=datetime.utcnow)
