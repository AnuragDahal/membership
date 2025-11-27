from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.subscriptions import Subscription
from app.schemas.subscriptions import SubscriptionCreate, SubscriptionResponse
from typing import List
from sqlalchemy import select
from datetime import datetime, timedelta
from app.models.plans import Plan


class SubscriptionService:
    def __init__(self, session: AsyncSession):
        self.session: AsyncSession = session

    async def create_subscription(self, subscription_data: SubscriptionCreate) -> Subscription:
        try:
            plan = await self.session.get(Plan, subscription_data.plan_id)
            if not plan:
                raise HTTPException(
                    detail="Plan not found", status_code=status.HTTP_404_NOT_FOUND
                )
            end_date = datetime.utcnow() + timedelta(days=plan.duration_days)
            new_subscription = Subscription(**subscription_data.model_dump())
            new_subscription.end_date = end_date
            self.session.add(new_subscription)
            await self.session.commit()
            await self.session.refresh(new_subscription)
            return new_subscription
        except Exception as e:
            raise HTTPException(detail=str(
                e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    async def get_member_subscription(self, member_id: int) -> Subscription | List[Subscription]:
        try:
            statement = select(Subscription).where(
                Subscription.member_id == member_id)
            result = await self.session.execute(statement)
            subscriptions = result.scalars().all()
            active_subscriptions = [
                subscription for subscription in subscriptions if subscription.end_date > datetime.utcnow()]
            if len(active_subscriptions) == 0:
                raise HTTPException(
                    detail="No active subscriptions found", status_code=status.HTTP_404_NOT_FOUND
                )
            return active_subscriptions
        except Exception as e:
            raise HTTPException(detail=str(
                e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
