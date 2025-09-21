from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped

# SQLAlchemy ORM models
class Base(DeclarativeBase):
    pass

class WinEntry(Base):
    __tablename__ = "win_entries"
    
    id: Mapped[int] = Column(Integer, primary_key=True) #type: ignore
    win: Mapped[str] = Column(String, nullable=False) #type: ignore
    created_at = Column(DateTime, default=datetime.now)

class MoodEntry(Base):
    __tablename__ = "mood_entries"
    
    id: Mapped[int] = Column(Integer, primary_key=True) #type: ignore
    mood: Mapped[str] = Column(String, nullable=False) #type: ignore
    created_at = Column(DateTime, default=datetime.now)

class ThoughtEntry(Base):
    __tablename__ = "thought_entries"
    
    id: Mapped[int] = Column(Integer, primary_key=True) #type: ignore
    thought: Mapped[str] = Column(String, nullable=False) #type: ignore
    created_at = Column(DateTime, default=datetime.now)
