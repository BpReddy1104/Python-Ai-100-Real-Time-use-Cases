# 📝 Blog Platform REST API with FastAPI

A RESTful API backend for a blog platform built using **FastAPI**, **SQLAlchemy**, and **Pydantic**. It supports full **CRUD operations** with clean modular architecture and automatic documentation using Swagger UI.

---

## 🚀 Features

- Create, Read, Update, Delete (CRUD) blog posts
- FastAPI for high-performance asynchronous web API
- SQLAlchemy ORM integration with SQLite (easy to switch to PostgreSQL)
- Pydantic models for request validation and response serialization
- Interactive Swagger docs at `/docs`
- Modular project structure: routers, schemas, models, database

---

## 🛠 Tech Stack

- **FastAPI**
- **SQLAlchemy**
- **Pydantic**
- **SQLite** (development)
- **Uvicorn** (ASGI server)

---

## 📂 Project Structure

```
fastapi_blog_platform/
│
├── main.py                # Entry point
├── database/
│   └── database.py        # DB connection
│   └── models.py          # SQLAlchemy models
├── routers/
│   └── blog.py            # Blog routes (CRUD)
├── schemas/
│   └── blog.py            # Pydantic schemas
└── requirements.txt       # Dependencies
```

---

## ▶️ How to Run

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/fastapi-blog-platform.git
   cd fastapi-blog-platform
   ```

2. **Create Virtual Environment (Optional)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the App**
   ```bash
   uvicorn main:app --reload
   ```

5. **Access Swagger Docs**
   - Go to: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 📬 API Endpoints

| Method | Endpoint        | Description             |
|--------|-----------------|-------------------------|
| GET    | `/blog`         | Get all blog posts      |
| GET    | `/blog/{id}`    | Get blog post by ID     |
| POST   | `/blog`         | Create new blog post    |
| PUT    | `/blog/{id}`    | Update blog post        |
| DELETE | `/blog/{id}`    | Delete blog post        |

---

## 🔧 Future Improvements

- Add JWT authentication
- Connect to PostgreSQL
- Deploy using Docker + Render
- Add comments & user models

---

## 💡 Author

- [Your Name](https://www.linkedin.com/in/your-profile)
