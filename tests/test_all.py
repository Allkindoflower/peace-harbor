import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base
from app import schemas
from app import crud
from app import models

# --- Setup in-memory SQLite ---
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create all tables
Base.metadata.create_all(bind=engine)

# mock db session
@pytest.fixture
def db():
    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.close()

# --- Win Tests ---
def test_add_win(db) -> None:
    win = schemas.WinEntry(win="deployed app")
    inserted_win = crud.create_win(db, win)
    assert inserted_win is not None
    assert inserted_win.win == "deployed app"
    assert isinstance(inserted_win.id, int)

def test_get_wins(db):
    crud.create_win(db, schemas.WinEntry(win="win1"))
    crud.create_win(db, schemas.WinEntry(win="win2"))
    
    skip, limit = 0, 10
    wins = crud.get_wins(db, skip, limit)
    
    all_wins = db.query(models.WinEntry).offset(skip).limit(limit).all()
    assert len(all_wins) == len(all_wins)
    assert wins[0].win == all_wins[0].win

def test_delete_win(db):
    win = schemas.WinEntry(win="became a president")
    inserted_win = crud.create_win(db, win)
    deleted_win = crud.delete_win(db, inserted_win.id)   
    assert deleted_win is True

    wins_after = crud.get_wins(db)
    assert len(wins_after) == 3

# --- Mood Tests ---
def test_add_mood(db):
    mood = schemas.MoodEntry(mood="Happy")
    created_mood = crud.create_mood(db, mood)
    assert created_mood.mood == "Happy"
    assert isinstance(created_mood.id, int)

def test_get_moods(db):
    crud.create_mood(db, schemas.MoodEntry(mood="Sad"))
    crud.create_mood(db, schemas.MoodEntry(mood="Excited"))
    
    skip, limit = 0, 10
    moods = crud.get_moods(db, skip, limit)
    
    all_moods = db.query(models.MoodEntry).offset(skip).limit(limit).all()
    assert len(all_moods) == len(all_moods)
    assert moods[0].mood == all_moods[0].mood

def test_delete_mood(db):
    mood = schemas.MoodEntry(mood="Angry")
    created_mood = crud.create_mood(db, mood)
    success = crud.delete_mood(db, created_mood.id)
    assert success is True

    moods_after = crud.get_moods(db)
    assert len(moods_after) == 3

# --- Thought Tests ---
def test_add_thought(db):
    thought_data = schemas.ThoughtEntry(thought="Test thought")
    created_thought = crud.create_thought(db, thought_data)
    assert created_thought.thought == "Test thought"
    assert isinstance(created_thought.id, int)

def test_get_thoughts(db):
    crud.create_thought(db, schemas.ThoughtEntry(thought="Thought 1"))
    crud.create_thought(db, schemas.ThoughtEntry(thought="Thought 2"))
    
    skip, limit = 0, 10
    thoughts = crud.get_thoughts(db, skip, limit)
    
    all_thoughts = db.query(models.ThoughtEntry).offset(skip).limit(limit).all()
    assert len(all_thoughts) == len(all_thoughts)
    assert thoughts[0].thought == all_thoughts[0].thought

def test_delete_thought(db):
    thought_data = schemas.ThoughtEntry(thought="Delete me")
    created_thought = crud.create_thought(db, thought_data)
    success = crud.delete_thought(db, created_thought.id)
    assert success is True

    thoughts_after = crud.get_thoughts(db)
    assert len(thoughts_after) == 3
