from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.db import get_db
from app.models.members import Member
from app.schemas.members import MemberCreate, MemberResponse


router = APIRouter()


@router.post("/member")
async def create_member(request: MemberCreate, db: AsyncSession = Depends(get_db)):
    try:
        member = db.query(Member).filter(Member.email == request.email).first()
        if member:
            raise HTTPException(
                detail="member already exisits", status_code=status.http
            )
        new_member = Member(**request.model_dump())
        await db.add(new_member)

    except Exception as e:
        raise HTTPException(detail=str(e), status_code=status.HTTP_409_CONFLICT)


@router.get("/members", response_model=List[MemberResponse])
async def get_member():
    try:
        pass
    except Exception as e:
        raise HTTPException(detail=str(e), status_code=500)
