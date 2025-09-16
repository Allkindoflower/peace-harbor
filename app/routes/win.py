#win.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas, crud
from app.database import get_db


router = APIRouter()


@router.post("/")
def add_win(win: schemas.WinEntry, db: Session = Depends(get_db)):
    return crud.create_win(db=db, win=win)

@router.get("/")
def get_wins(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_wins(db, skip=skip, limit=limit)
