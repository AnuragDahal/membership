from fastapi import FastAPI

from app.api import attendance, members, plans, subscriptions

app = FastAPI(title="Membership API")


app.include_router(members.router, prefix="/members", tags=["members"])
app.include_router(plans.router, prefix="/plans", tags=["plans"])
app.include_router(
    subscriptions.router, prefix="/subscriptions", tags=["subscriptions"]
)
app.include_router(attendance.router, prefix="/attendance", tags=["attendance"])


@app.get("/")
def read_root():
    return {"message": "Hello from membership!"}
