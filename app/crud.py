# crud.py
from sqlalchemy.orm import Session
from . import models, schemas


def create_win(db: Session, win: schemas.WinEntry):
    db_win = models.WinEntry(win=win.win)
    db.add(db_win)
    db.commit()
    db.refresh(db_win)
    return db_win

def get_wins(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.WinEntry).offset(skip).limit(limit).all()


def create_mood(db: Session, mood: schemas.MoodEntry):
    db_mood = models.MoodEntry(mood=mood.mood)
    db.add(db_mood)
    db.commit()
    db.refresh(db_mood)
    return db_mood

def get_moods(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.MoodEntry).offset(skip).limit(limit).all()


def create_thought(db: Session, thought: schemas.ThoughtEntry):
    db_thought = models.ThoughtEntry(thought=thought.thought)
    db.add(db_thought)
    db.commit()
    db.refresh(db_thought)
    return db_thought

def get_thoughts(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.ThoughtEntry).offset(skip).limit(limit).all()

