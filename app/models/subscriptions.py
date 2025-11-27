from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional

class Subscription(SQLModel, table=True):
    __tablename__ = "subscriptions"
    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    member_id: int = Field(foreign_key="members.id", index=True)
    plan_id: int = Field(foreign_key="plans.id", index=True)
    start_date: datetime = Field(default_factory=datetime.utcnow)
    end_date: Optional[datetime] = Field(default=None)