from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.core.db import engine, Base
from app.api import members, plans, subscriptions

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Create tables on startup (for development)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    # Close connection on shutdown
    await engine.dispose()

app = FastAPI(title="Membership API", lifespan=lifespan)


app.include_router(members.router, prefix="/members", tags=["members"])
app.include_router(plans.router, prefix="/plans", tags=["plans"])
app.include_router(subscriptions.router,
                   prefix="/subscriptions", tags=["subscriptions"])


@app.get("/")
def read_root():
    return {"message": "Hello from membership!"}
