from fastapi import APIRouter, HTTPException, status, Depends
from app.core.db import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.subscriptions import SubscriptionCreate, SubscriptionResponse

router = APIRouter()


@router.post("/subscriptions", status_code=status.HTTP_201_CREATED)
async def create_subscription(
    request: SubscriptionCreate, db: AsyncSession = Depends(get_db)
):
    try:
        pass
    except Exception as e:
        raise HTTPException(
            detail=str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@router.post(
    f"/members/{id}/current-subscriptions",
    response_model=SubscriptionResponse,
    status_code=status.HTTP_201_CREATED,
)
async def get_subscription(
    request: SubscriptionCreate, db: AsyncSession = Depends(get_db)
):
    try:
        pass
    except Exception as e:
        raise HTTPException(
            detail=str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
