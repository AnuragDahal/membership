from sqlalchemy import Column, Integer, String, VARCHAR, DATETIME, Enum
from app.core.db import Base
from datetime import datetime

class Member(Base):
    __tablename__ = "members"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    phone = Column(VARCHAR(15))
    join_date = Column(DATETIME, default=datetime.utcnow())
    status = Column(Enum("active", "inactive"))
    total_checkins = Column(Integer, default=0)