# 📌 FastAPI Task Management API

A simple RESTful API built with **FastAPI** and **SQLite** that demonstrates CRUD operations, database integration, and API documentation with Swagger.  

---

## 🚀 Features
- Create, Read, Update, and Delete (CRUD) tasks  
- SQLite database integration using SQLAlchemy  
- Input validation with Pydantic  
- Interactive API docs with Swagger (`/docs`) and ReDoc (`/redoc`)  
- Error handling for missing/invalid data  

---

## 🛠 Tech Stack
- **FastAPI** (for building API)  
- **Uvicorn** (ASGI server)  
- **SQLAlchemy** (ORM for database)  
- **Pydantic** (data validation)  
- **SQLite** (default database, can be replaced with PostgreSQL/MySQL)  

---

## 📂 Project Structure
```
fast-api-tasks/
│── app.py          # Main entry point
│── models.py       # Database models
│── schemas.py      # Pydantic schemas
│── crud.py         # CRUD operations
│── database.py     # DB session & engine
│── requirements.txt # Dependencies
│── README.md       # Project documentation
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/fast-api-tasks.git
cd fast-api-tasks
```

### 2️⃣ Create & activate virtual environment
```bash
python -m venv .venv
# Activate
.venv\Scripts\activate   # Windows
source .venv/bin/activate # Linux/Mac
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the server
```bash
uvicorn app:app --reload
```

### 5️⃣ Open in browser
- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  
- ReDoc UI: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)  

---

## 📝 API Endpoints

### 🔹 Create Task
```
POST /tasks/
```

### 🔹 Get All Tasks
```
GET /tasks/
```

### 🔹 Get Task by ID
```
GET /tasks/{task_id}
```

### 🔹 Update Task
```
PUT /tasks/{task_id}
```

### 🔹 Delete Task
```
DELETE /tasks/{task_id}
```

---

## 📦 Deployment (Optional)
You can deploy with Docker:
```bash
docker build -t fastapi-tasks .
docker run -d -p 8000:8000 fastapi-tasks
```

---

## 🙌 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss.  

---

## 📜 License
This project is licensed under the MIT License.  
