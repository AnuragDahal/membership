from typing import List
from fastapi import APIRouter, HTTPException, status

from app.schemas.plans import PlanCreate, PlanResponse

router = APIRouter()


@router.post("/plans", status_code=status.HTTP_201_CREATED)
async def create_plan(request: PlanCreate):
    try:
        pass
    except Exception as e:
        raise HTTPException(
            detail=str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@router.get("/plans", response_model=List[PlanResponse], status_code=status.HTTP_200_OK)
async def get_plans():
    try:
        pass
    except Exception as e:
        raise HTTPException(
            detail=str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
