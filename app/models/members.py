from sqlalchemy import Column, Integer, String, DateTime, Enum
from app.core.db import Base
from datetime import datetime
import enum

class MemberStatus(str, enum.Enum):
    active = "active"
    inactive = "inactive"

class Member(Base):
    __tablename__ = "members"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    phone = Column(String(15))
    join_date = Column(DateTime, default=datetime.utcnow)
    status = Column(Enum(MemberStatus), default=MemberStatus.active)
    total_checkins = Column(Integer, default=0)