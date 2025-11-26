from pydantic import BaseModel
from datetime import datetime

class MemberCreate(BaseModel):
    name: str
    email: str
    phone: str

class MemberUpdate(BaseModel):
    name: str
    email: str
    phone: str

class MemberResponse(BaseModel):
    id: int
    name: str
    email: str
    phone: str
    join_date: datetime
    status: str
    total_checkins: int

    class Config:
        orm_mode = True
