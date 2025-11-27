from pydantic import BaseModel, ConfigDict
from datetime import datetime


class AttendanceCreate(BaseModel):
    member_id: int


class AttendanceResponse(BaseModel):
    id: int
    member_id: int
    check_in: datetime

    model_config = ConfigDict(from_attributes=True)
