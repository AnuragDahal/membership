from sqlmodel import Field, SQLModel
from datetime import datetime
from typing import Optional

class Member(SQLModel, table=True):
    __tablename__ = "members"
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=100)
    email: str = Field(max_length=100)
    phone: str = Field(max_length=15, min_length=10)
    join_date: datetime = Field(default_factory=datetime.utcnow)
    status: str = Field(default="active")
    total_checkins: int = Field(default=0)
