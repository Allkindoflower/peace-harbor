from pydantic import BaseModel
from typing import Optional


#pydantic models for input validation
class WinEntry(BaseModel):
    win: str

    
class MoodEntry(BaseModel):
    mood: str
    sentiment: Optional[str] = None

    
class ThoughtEntry(BaseModel):
    thought: str
