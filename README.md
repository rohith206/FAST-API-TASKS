# FAST-API-TASKS
RESTful API built with FastAPI to manage tasks. Implements full CRUD functionality, SQLite database integration with SQLAlchemy, and input validation using Pydantic. Includes Swagger UI for API documentation.
# FastAPI Task Management API

A RESTful API built with **FastAPI** to manage tasks.

## 🚀 Features
- CRUD operations (Create, Read, Update, Delete tasks)
- SQLite database using SQLAlchemy ORM
- Input validation with Pydantic
- Automatic API docs with Swagger (http://127.0.0.1:8000/docs)

## 🛠️ Tech Stack
- Python 3
- FastAPI
- SQLAlchemy
- Pydantic
- SQLite

## 📦 Installation

```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd fastapi-task-api
python -m venv .venv
.venv\Scripts\activate   # On Windows
pip install -r requirements.txt
