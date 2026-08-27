````markdown
# ExpenseFlow

A RESTful expense tracker API built with Django REST Framework and MySQL. Users can securely manage their personal expenses using JWT authentication.

## Features

- User registration and JWT authentication
- Create, read, update, and delete expenses
- User-specific expense management
- Filter expenses by:
  - Past week
  - Past month
  - Last 3 months
  - Custom date range

## Tech Stack

- Python
- Django
- Django REST Framework
- MySQL
- JWT
- python-decouple
- uv

## Setup

```bash
git clone https://github.com/mucheru-delvan/ExpenseFlow.git
cd ExpenseFlow
uv sync
source .venv/bin/activate
python manage.py migrate
python manage.py runserver
````

Create a `.env` file with your MySQL and Django configuration before running the project.

## API

```text
POST   /api/auth/register/
POST   /api/auth/token/
POST   /api/auth/token/refresh/

GET    /api/expenses/
POST   /api/expenses/
GET    /api/expenses/<id>/
PATCH  /api/expenses/<id>/
DELETE /api/expenses/<id>/
```

Built as a backend project to practice Django REST Framework, JWT authentication, MySQL, and API development.

```

**This is the version I'd actually put on your GitHub.** It tells someone what the project is, what it does, what it's built with, and how to start it without turning the README into a manual.
```
