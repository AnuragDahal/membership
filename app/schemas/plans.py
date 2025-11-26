from pydantic import BaseModel

class PlanCreate(BaseModel):
    name: str
    price: int
    duration_days: int

class PlanUpdate(BaseModel):
    name: str
    price: int
    duration_days: int

class PlanResponse(BaseModel):
    id: int
    name: str
    price: int
    duration_days: int
    