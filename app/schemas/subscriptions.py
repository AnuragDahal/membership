from pydantic import BaseModel
from datetime import datetime

class SubscriptionCreate(BaseModel):
    member_id: int
    plan_id: int

class SubscriptionUpdate(BaseModel):
    member_id: int
    plan_id: int

class SubscriptionResponse(BaseModel):
    id: int
    member_id: int
    plan_id: int
    start_date: datetime
    end_date: datetime

    class Config:
        orm_mode = True