# Peace Harbor – Manage Your Emotions

A modern FastAPI application for tracking daily wins, moods, and thoughts. Built with SQLite for persistence and designed with clean architecture principles for maintainability and scalability.

## ✨ Features

- **Win Tracking**: Log daily achievements and victories
- **Mood Monitoring**: Record and track emotional states over time
- **Thought Journaling**: Capture ideas, reflections, and notes
- **RESTful API**: Clean, intuitive endpoints following REST principles
- **Type Safety**: Full type hints throughout the codebase
- **Comprehensive Logging**: Built-in logging for debugging and monitoring
- **SQLite Backend**: Lightweight, serverless database solution
- **Test Coverage**: Comprehensive unit tests for all CRUD operations

## 🏗️ Architecture

```
peace-harbor/
├── app/
│   ├── routes/           # API route handlers
│   │   ├── win.py        # Win-related endpoints
│   │   ├── mood.py       # Mood-related endpoints
│   │   └── thought.py    # Thought-related endpoints
│   ├── crud.py           # Database operations layer
│   ├── models.py         # SQLAlchemy ORM models
│   ├── schemas.py        # Pydantic request/response schemas
│   └── main.py           # Application entry point
├── tests/                # Unit tests for CRUD operations
├── stressed_out.db       # SQLite database (development only)
├── requirements.txt      # Python dependencies
├── README.md
└── LICENSE
```

> **Note**: Virtual environments, cache files, and other temporary artifacts are ignored via `.gitignore`.

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- pip package manager

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Allkindoflower/peace-harbor
   cd peace-harbor
   ```

2. **Set up a virtual environment:**
   ```bash
   python -m venv venv
   
   # Activate the virtual environment
   source venv/bin/activate     # macOS/Linux
   venv\Scripts\activate        # Windows
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Start the development server:**
   ```bash
   uvicorn app.main:app --reload
   ```

The API will be running at `http://127.0.0.1:8000/`

Interactive API documentation is available at `http://127.0.0.1:8000/docs`

## 📖 API Usage

### Wins Endpoints

**Create a new win:**
```http
POST /wins
Content-Type: application/json

{
  "win": "Successfully deployed my first FastAPI application"
}
```

**Retrieve all wins:**
```http
GET /wins
```

**Delete a specific win:**
```http
DELETE /wins/{win_id}
```

### Moods Endpoints

```http
POST /moods       # Create a mood entry
GET /moods        # Retrieve all mood entries
DELETE /moods/{id} # Delete a specific mood entry
```

### Thoughts Endpoints

```http
POST /thoughts       # Create a thought entry
GET /thoughts        # Retrieve all thought entries
DELETE /thoughts/{id} # Delete a specific thought entry
```

All endpoints follow the same CRUD pattern: `POST` to create, `GET` to fetch all, and `DELETE /{id}` to remove specific entries.

## 🧪 Testing

Run the complete test suite:

```bash
# Ensure virtual environment is active
pytest

# Run with coverage report
pytest --cov=app

# Run a specific test file
pytest tests/test_crud.py -v
```

Tests cover all CRUD operations and use isolated database sessions to prevent conflicts.

## 🛠️ Development

### Code Style

- Full type hints throughout the codebase
- Comprehensive logging for debugging
- Clean separation of concerns (routes, CRUD, models, schemas)
- SQLAlchemy ORM with proper type casting

### Database

The application uses SQLite (`stressed_out.db`) for development and testing.

> **Important**: The database file is intended for local development only. Do not commit production databases.

### Type Checking

SQLAlchemy ORM type hints can produce false positives with some static type checkers. Use `cast()` or `# type: ignore` where appropriate to satisfy type checkers without breaking runtime behavior.

## 🤝 Contributing

We welcome contributions! Follow these steps to contribute:

1. **Fork the repository** on GitHub

2. **Create a feature branch:**
   ```bash
   git checkout -b feature/my-feature
   ```

3. **Implement changes** and add tests if needed

4. **Commit changes** with descriptive messages:
   ```bash
   git commit -m "feat(wins): add validation for win length"
   git commit -m "fix(moods): handle edge case in mood deletion"
   ```

5. **Push and open a Pull Request:**
   ```bash
   git push origin feature/my-feature
   ```

### Commit Message Format

- `feat(scope): description` - New features
- `fix(scope): description` - Bug fixes
- `docs(scope): description` - Documentation updates
- `test(scope): description` - Test additions/updates

## 📄 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

**Built with FastAPI, SQLAlchemy, and modern Python practices.**