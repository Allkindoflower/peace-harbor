#main.py
from fastapi import FastAPI
from app.routes import thought, win, mood
from app.database import engine
from app.models import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(win.router, prefix="/wins", tags=["wins"])
app.include_router(mood.router, prefix="/moods", tags=["moods"])
app.include_router(thought.router, prefix="/thoughts", tags=["thought"])



