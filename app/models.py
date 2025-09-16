from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

#SQLAlchemy ORM models

Base = declarative_base()

class WinEntry(Base):
    __tablename__ = "win_entries"
    id = Column(Integer, primary_key=True)
    win = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now)

class MoodEntry(Base):
    __tablename__ = "mood_entries" 
    id = Column(Integer, primary_key=True)
    mood = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now)

class ThoughtEntry(Base):
    __tablename__ = "thought_entries"  
    id = Column(Integer, primary_key=True)
    thought = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now)
