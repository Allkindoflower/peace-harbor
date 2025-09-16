#mood.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas, crud
from app.database import get_db


router = APIRouter()


@router.post("/")
def add_mood(mood: schemas.MoodEntry, db: Session = Depends(get_db)):
    return crud.create_mood(db=db, mood=mood)

@router.get("/")
def get_moods(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_moods(db, skip=skip, limit=limit)
