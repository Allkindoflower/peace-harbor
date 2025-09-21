# crud.py
from sqlalchemy.orm import Session
from typing import List
from . import models, schemas
import logging

logger = logging.getLogger(__name__)

# -------------------------
# Wins CRUD
# -------------------------
def create_win(db: Session, win: schemas.WinEntry) -> models.WinEntry:
    db_win = models.WinEntry(win=win.win)
    db.add(db_win)
    db.commit()
    db.refresh(db_win)
    logger.info(f"Win created with ID {db_win.id}")
    return db_win

def get_wins(db: Session, skip: int = 0, limit: int = 10) -> List[models.WinEntry]:
    return db.query(models.WinEntry).offset(skip).limit(limit).all()

def delete_win(db: Session, win_id: int) -> bool:
    db_win = db.query(models.WinEntry).filter(models.WinEntry.id == win_id).first()
    if not db_win:
        logger.error(f"Deleting win failed: ID {win_id} not found")
        return False
    db.delete(db_win)
    db.commit()
    logger.info(f"Win ID {win_id} deleted successfully")
    return True

# -------------------------
# Moods CRUD
# -------------------------
def create_mood(db: Session, mood: schemas.MoodEntry) -> models.MoodEntry:
    db_mood = models.MoodEntry(mood=mood.mood)
    db.add(db_mood)
    db.commit()
    db.refresh(db_mood)
    logger.info(f"Mood created with ID {db_mood.id}")
    return db_mood

def get_moods(db: Session, skip: int = 0, limit: int = 10) -> List[models.MoodEntry]:
    return db.query(models.MoodEntry).offset(skip).limit(limit).all()

def delete_mood(db: Session, mood_id: int) -> bool:
    db_mood = db.query(models.MoodEntry).filter(models.MoodEntry.id == mood_id).first()
    if not db_mood:
        logger.error(f"Deleting mood failed: ID {mood_id} not found")
        return False
    db.delete(db_mood)
    db.commit()
    logger.info(f"Mood ID {mood_id} deleted successfully")
    return True

# -------------------------
# Thoughts CRUD
# -------------------------
def create_thought(db: Session, thought: schemas.ThoughtEntry) -> models.ThoughtEntry:
    db_thought = models.ThoughtEntry(thought=thought.thought)
    db.add(db_thought)
    db.commit()
    db.refresh(db_thought)
    logger.info(f"Thought created with ID {db_thought.id}")
    return db_thought

def get_thoughts(db: Session, skip: int = 0, limit: int = 10) -> List[models.ThoughtEntry]:
    return db.query(models.ThoughtEntry).offset(skip).limit(limit).all()

def delete_thought(db: Session, thought_id: int) -> bool:
    db_thought = db.query(models.ThoughtEntry).filter(models.ThoughtEntry.id == thought_id).first()
    if not db_thought:
        logger.error(f"Deleting thought failed: ID {thought_id} not found")
        return False
    db.delete(db_thought)
    db.commit()
    logger.info(f"Thought ID {thought_id} deleted successfully")
    return True
