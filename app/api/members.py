from typing import List, Union
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.db import get_db
from app.models.members import Member
from app.schemas.members import MemberCreate, MemberResponse
from app.services.members import MemberService

router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_member(request: MemberCreate, db: AsyncSession = Depends(get_db)):
    try:
        member = await MemberService(db).create_member(request)
        return {"message": "Member created successfully", "member": member}

    except Exception as e:
        raise HTTPException(detail=str(
            e), status_code=status.HTTP_409_CONFLICT)


@router.get("/", response_model=List[MemberResponse], status_code=status.HTTP_200_OK)
async def get_members(db: AsyncSession = Depends(get_db)):
    try:
        members = await MemberService(db).get_all_members()
        return members
    except Exception as e:
        raise HTTPException(detail=str(
            e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
