from sqlalchemy import Column, Integer, String, VARCHAR
from app.db import Base


class Subscription(Base):
    __tablename__ = "subscriptions"
    id = Column(Integer, primary_key=True, index=True)
    member_id = Column(Integer,ForeignKey("members.id"), index=True)
    plan_id = Column(Integer,ForeignKey("plans.id"), index=True)
    start_date = Column(DATETIME, default=datetime.utcnow())
    end_date = Column()

relationship("subscriptions", back_populates="member",cascade="all, delete-orphan")