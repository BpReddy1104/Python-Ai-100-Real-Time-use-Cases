
# 📝 To-Do App with Django

## 📅 Day 2 - Python 100 Days, 100 Projects

A simple yet functional task manager built using Django. This app allows users to create, view, update, and delete their to-do tasks using Django ORM and views.

---

## 🛠️ Tech Stack

- **Backend:** Django (Python)
- **Database:** SQLite (default Django database)
- **Frontend:** Django templates (HTML)

---

## 📂 Project Structure

```
todo_project/
├── manage.py
├── todo_project/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── tasks/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   │   └── tasks/
│   │       ├── task_list.html
│   │       └── task_form.html
└── db.sqlite3
```

---

## 🚀 How to Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/django-todo-app.git
cd django-todo-app
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate


### 3. Install dependencies

pip install -r requirements.txt


### 4. Run migrations

python manage.py migrate


### 5. Start the development server

python manage.py runserver


Then open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

---

## ✍️ Features

- Add new tasks
- View a list of tasks
- Edit existing tasks
- Delete tasks
- Mark tasks as complete/incomplete (optional feature)

---

## 🧪 Testing

Basic functionality can be tested manually through the UI.
You may extend this project by adding:
- User authentication
- Task priority & due dates
- API support via Django REST Framework

---


## 🙌 Acknowledgements

Part of the **"Python 100 Days, 100 Projects"** learning challenge.
