from sqlmodel import SQLModel, Field
from typing import Optional

class Plan(SQLModel, table=True):
    __tablename__ = "plans"
    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    name: str = Field(index=True)
    price: int
    duration_days: int
