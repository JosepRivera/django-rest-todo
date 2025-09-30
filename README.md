# Django REST ToDo ✅

A clean and minimal **ToDo management REST API** built with **Django** and **Django REST Framework**.
This project demonstrates best practices for building a RESTful API, including authentication, permissions, filtering, and pagination.

---

## 🚀 Features

- 🔑 **User authentication** with JWT (JSON Web Tokens).
- 📝 **CRUD operations** for tasks (create, list, update, delete).
- 🔒 **Custom permissions**: users can only manage their own tasks.
- 🔍 **Filtering & searching** tasks by status, title, or description.
- 📄 **Pagination** for large task lists.
- 🧩 Extensible project structure for future features.

---

## 🛠️ Tech Stack

- **Python 3.10+**
- **Django 5+**
- **Django REST Framework**
- **Simple JWT** for authentication
- **django-filter** for query filtering
- **SQLite** (default, easy to replace with PostgreSQL or MySQL)

---

## ⚙️ Installation

1. **Clone repository:**

```bash
git clone https://github.com/yourusername/django-rest-todo.git
cd django-rest-todo
```

2. **Create virtual environment:**

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

4. **Apply migrations:**

```bash
python manage.py migrate
```

5. **Create superuser (admin account):**

```bash
python manage.py createsuperuser
```

6. **Run development server:**

```bash
python manage.py runserver
```

---

## 🔑 Authentication

This project uses **JWT (JSON Web Tokens)**:

- `POST /api/token/` → obtain access & refresh tokens
- `POST /api/token/refresh/` → refresh access token

You must include the token in the **Authorization header**:

```http
Authorization: Bearer <your_token>
```

---

## 📌 API Endpoints

### Users

- `POST /api/register/` → Register a new user
- `POST /api/token/` → Login with JWT

### Tasks

- `GET /api/tasks/` → List tasks of authenticated user
- `POST /api/tasks/` → Create a new task
- `GET /api/tasks/{id}/` → Retrieve task details
- `PUT/PATCH /api/tasks/{id}/` → Update a task
- `DELETE /api/tasks/{id}/` → Delete a task

---

## 🔍 Filtering & Pagination

- Filter by status: `/api/tasks/?status=pending`
- Search by title or description: `/api/tasks/?search=keyword`
- Order by creation date: `/api/tasks/?ordering=-created_at`
- Paginated results: `/api/tasks/?page=2`

---

## 🧪 Testing

You can test endpoints using:

- [Postman](https://www.postman.com/)
- [Insomnia](https://insomnia.rest/)
- Django REST Framework’s built-in **Browsable API**

---

💡 _This repository is designed as a learning project to practice Django REST Framework. It can be extended into a full production-ready ToDo application with a frontend (React, Vue, or mobile app) consuming this API._
