from typing import List

from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.members import Member
from app.schemas.members import MemberCreate, MemberResponse


class MemberService:

    def __init__(self, session: AsyncSession):
        self.session: AsyncSession = session

    async def create_member(self, member_data: MemberCreate) -> Member:

        try:
            statement = select(Member).where(Member.email == member_data.email)
            result = await self.session.execute(statement)
            member = result.scalar_one_or_none()
            if member:
                raise HTTPException(
                    detail="Member already exists",
                    status_code=status.HTTP_400_BAD_REQUEST,
                )
            new_member = Member(**member_data.model_dump())
            await self.session.add(new_member)
            await self.session.commit()
            await self.session.refresh(new_member)
            return new_member
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(
                detail=str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    async def get_all_members(self) -> List[Member]:
        try:
            statement = select(Member)
            result = await self.session.execute(statement)
            members = result.scalars().all()
            return [MemberResponse(**member.model_dump()) for member in members]
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(
                detail=str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
