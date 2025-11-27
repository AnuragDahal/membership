from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends, HTTPException, status
from app.core.db import get_db
from app.schemas.members import MemberCreate


class MemberService:

    def __init__(self):
        self.session: AsyncSession = Depends(get_db)

    async def create_member(member_data: MemberCreate):

        try:
            
            pass
        except Exception as e:
            raise HTTPException(
                detail=str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    