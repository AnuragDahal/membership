from fastapi import APIRouter, status, Depends
from app.services.plans import PlanService
from app.schemas.plans import PlanCreate
from app.core.db import get_db
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_plan(request: PlanCreate, db: AsyncSession = Depends(get_db)):
    plan = await PlanService(db).create_plan(request)
    return {"message": "Plan created successfully", "plan": plan}


@router.get("/", status_code=status.HTTP_200_OK)
async def get_plans(db: AsyncSession = Depends(get_db)):
    plans = await PlanService(db).get_all_plans()
    return {"message": "Plans fetched successfully", "plans": plans}
