#win.py
from fastapi import APIRouter, Depends
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from app import crud
from app.database import get_db


router = APIRouter()


@router.post("/add-win")
async def add_win(win, db: Session = Depends(get_db)):
    return crud.create_win(db, win)
    

@router.get("/get-wins")
def fetch_wins(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_wins(db, skip=skip, limit=limit)

@router.delete("/delete")
def remove_win(win_id: int, db: Session = Depends(get_db)):
    return crud.delete_win(db, win_id)