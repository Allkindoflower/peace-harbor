#main.py
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routes import thought, win, mood
from app.database import engine
from fastapi.responses import FileResponse
from app.models import Base


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


app.include_router(win.router, prefix="/wins", tags=["wins"])
app.include_router(mood.router, prefix="/moods", tags=["moods"])
app.include_router(thought.router, prefix="/thoughts", tags=["thought"])


@app.get("/")
async def home():
    return FileResponse("static/index.html")

