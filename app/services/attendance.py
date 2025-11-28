from sqlalchemy.ext.asyncio import AsyncSession
from app.core.db import get_db
from fastapi import Depends, HTTPException
from app.models.attendance import Attendance
from app.schemas.attendance import AttendanceCreate
from sqlalchemy import select
from datetime import datetime
from typing import List
from app.services.subscriptions import SubscriptionService


class AttendanceService:
    def __init__(self, session: AsyncSession = Depends(get_db)):
        self.session = session

    async def create_attendance(self, attendance: AttendanceCreate) -> Attendance:
        try:
            member_id = attendance.member_id
            active_subscriptions = await SubscriptionService(
                self.session
            ).get_member_subscription(member_id)
            if not active_subscriptions:
                raise HTTPException(
                    status_code=404, detail="No active subscriptions found"
                )
            new_entry = Attendance(**attendance.model_dump())
            entry_time = datetime.utcnow()
            new_entry.check_in = entry_time
            self.session.add(new_entry)
            await self.session.commit()
            await self.session.refresh(new_entry)
            return new_entry
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    async def get_attendance(self, member_id: int) -> List[Attendance]:
        try:
            statement = select(Attendance).where(Attendance.member_id == member_id)
            result = await self.session.execute(statement)
            attendance = result.scalars().all()
            if not attendance:
                raise HTTPException(status_code=404, detail="Attendance not found")
            return attendance
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
