from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.core.db import engine
from app.api import members, plans, subscriptions
from sqlmodel import SQLModel
from app.api import attendance
from alembic.config import Config
from alembic import command
import asyncio
import concurrent.futures

executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)


def run_migrations():
    alembic_cfg = Config("alembic.ini")
    command.upgrade(alembic_cfg, "head")


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Run alembic migrations on startup
    loop = asyncio.get_event_loop()
    # Run Alembic migrations in separate thread
    await loop.run_in_executor(executor, run_migrations)
    print("Alembic migrations applied successfully.")
    yield
    # Close connection on shutdown
    print("Closing connection")

    await engine.dispose()

app = FastAPI(title="Membership API", lifespan=lifespan)


app.include_router(members.router, prefix="/members", tags=["members"])
app.include_router(plans.router, prefix="/plans", tags=["plans"])
app.include_router(subscriptions.router,
                   prefix="/subscriptions", tags=["subscriptions"])
app.include_router(attendance.router,
                   prefix="/attendance", tags=["attendance"])


@app.get("/")
def read_root():
    return {"message": "Hello from membership!"}
