from sqlmodel import Field, SQLModel
from datetime import datetime
from typing import Optional

class Attendance(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    member_id: int = Field(foreign_key="members.id", index=True)
    check_in: datetime = Field(default_factory=datetime.utcnow)
