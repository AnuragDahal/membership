from fastapi import APIRouter, status, Depends
from app.core.db import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.subscriptions import SubscriptionCreate
from app.services.subscriptions import SubscriptionService

router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_subscription(
    request: SubscriptionCreate, db: AsyncSession = Depends(get_db)
):
    subscription = await SubscriptionService(db).create_subscription(request)
    return {
        "message": "Subscription created successfully",
        "subscription": subscription,
    }


@router.get(
    "/member/{id}/current-subscriptions",
    status_code=status.HTTP_201_CREATED,
)
async def get_subscription(id: int, db: AsyncSession = Depends(get_db)):

    subscription = await SubscriptionService(db).get_member_subscription(id)
    return {
        "message": "Subscription fetched successfully",
        "subscription": subscription,
    }
