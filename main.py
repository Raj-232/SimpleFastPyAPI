from fastapi import FastAPI
from database import Base,engine
from routes.user import userrouter

Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(
    userrouter,
    prefix="/api/v1",
    tags=["users"],
)

