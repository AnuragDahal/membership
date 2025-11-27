from fastapi import APIRouter
from app.schemas.attendance import AttendanceCreate
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.db import get_db
from app.services.attendance import AttendanceService
from fastapi import HTTPException, Depends

router = APIRouter()


@router.post("/")
async def create_attendance(request: AttendanceCreate, db: AsyncSession = Depends(get_db)):
    try:
        attendance = await AttendanceService(db).create_attendance(request)
        return {"message": "Attendance created successfully", "data": attendance}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get('/{member_id}')
async def get_attendance(member_id: int, db: AsyncSession = Depends(get_db)):
    try:
        attendance = await AttendanceService(db).get_attendance(member_id)
        return {"message": "Attendance found", "data": attendance}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
