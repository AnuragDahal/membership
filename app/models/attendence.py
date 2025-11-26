from sqlalchemy import Column, Integer, String, VARCHAR, DATETIME, Enum, ForeignKey
from app.core.db import Base
from datetime import datetime
from sqlalchemy.orm import relationship

class Attendence(Base):
    __tablename__ = "attendence"
    id = Column(Integer, primary_key=True, index=True)
    member_id = Column(Integer,ForeignKey("members.id"), index=True)
    check_in = Column(DATETIME, default=datetime.utcnow())