from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.core.db import engine
from app.api import members, plans, subscriptions
from sqlmodel import SQLModel
from app.api import attendance


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await engine.dispose()


app = FastAPI(title="Membership API", lifespan=lifespan)


app.include_router(members.router, prefix="/members", tags=["members"])
app.include_router(plans.router, prefix="/plans", tags=["plans"])
app.include_router(
    subscriptions.router, prefix="/subscriptions", tags=["subscriptions"]
)
app.include_router(attendance.router, prefix="/attendance", tags=["attendance"])


@app.get("/")
def read_root():
    return {"message": "Hello from membership!"}
