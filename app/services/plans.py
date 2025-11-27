from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.plans import Plan
from app.schemas.plans import PlanCreate
from typing import List
from sqlalchemy import select


class PlanService:
    def __init__(self, session: AsyncSession):
        self.session: AsyncSession = session

    async def create_plan(self, plan_data: PlanCreate) -> Plan:
        try:
            statement = select(Plan).where(Plan.name == plan_data.name)
            result = await self.session.execute(statement)
            plan = result.scalar_one_or_none()
            if plan:
                raise HTTPException(
                    detail="Plan already exists", status_code=status.HTTP_400_BAD_REQUEST
                )
            new_plan = Plan(**plan_data.model_dump())
            self.session.add(new_plan)
            await self.session.commit()
            await self.session.refresh(new_plan)
            return new_plan
        except Exception as e:
            raise HTTPException(detail=str(
                e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    async def get_all_plans(self) -> List[Plan]:
        try:
            statement = select(Plan)
            result = await self.session.execute(statement)
            plans = result.scalars().all()
            return plans
        except Exception as e:
            raise HTTPException(detail=str(
                e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
