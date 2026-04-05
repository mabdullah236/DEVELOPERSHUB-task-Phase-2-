```markdown
# Bookstore API - Phase 2 Task

# Project Overview
This project is a RESTful API built for a Bookstore. It allows users to perform
CRUD (Create, Read, Update, Delete) operations on a database of books.This was created as part of the DEVELOPERSHUB Backend Development Internship (Phase 2).

# Technologies Used
* **Backend Framework:** Django, Django REST Framework (DRF)
* **Language:** Python
* **Database:** SQLite / MySQL 
* **API Testing Tool:** Postman
* **Version Control:** Git & GitHub

# How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/mabdullah236/DEVELOPERSHUB-task-Phase-2-.git](https://github.com/mabdullah236/DEVELOPERSHUB-task-Phase-2-.git)
   cd bookstore_api
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv env
   env\Scripts\activate  
   ```

3. **Install required dependencies:**
   ```bash
   pip install django djangorestframework
   ```

4. **Apply database migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run the development server:**
   ```bash
   python manage.py runserver
   ```
   *The server will start at `http://127.0.0.1:8000/`*

# API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/api/books/` | Add a new book to the database |
| `GET` | `/api/books/` | Fetch all books from the database |
| `GET` | `/api/books/<id>/` | Fetch one specific book by its ID |
| `PUT` | `/api/books/<id>/` | Update a specific book's details |
| `DELETE` | `/api/books/<id>/` | Remove a book from the database |

### Sample JSON Input (For POST and PUT requests)
```json
{
  "title": "Atomic Habits",
  "author": "James Clear",
  "price": 20,
  "isbn": "1234567890",
  "publishedDate": "2018-10-16"
}
```
```
