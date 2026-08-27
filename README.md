# ExpenseFlow

A RESTful Expense Tracker API built with Django REST Framework and MySQL. Users can authenticate with JWT and manage their personal expenses.

## Features

- User registration and JWT authentication
- Create, retrieve, update, and delete expenses
- User-specific expense management
- Filter expenses by:
  - Past week
  - Past month
  - Last 3 months
  - Custom date range
- MySQL database integration
- Environment configuration with `python-decouple`

## Tech Stack

- Python
- Django
- Django REST Framework
- MySQL
- JWT
- python-decouple
- uv
- Postman

## Project Structure

```text
ExpenseFlow/
├── expenseflow/
├── expenses/
├── users/
├── manage.py
├── pyproject.toml
├── uv.lock
├── .gitignore
└── README.md
````

## Getting Started

### Clone the repository

```bash
git clone https://github.com/mucheru-delvan/ExpenseFlow.git
cd ExpenseFlow
```

### Install dependencies

```bash
uv sync
source .venv/bin/activate
```

### Configure environment variables

Create a `.env` file:

```env
SECRET_KEY=your-secret-key

DB_NAME=expense_flow
DB_USER=expense_flow_user
DB_PASSWORD=your-mysql-password
DB_HOST=localhost
DB_PORT=3306
```

### Run migrations

```bash
python manage.py migrate
```

### Start the server

```bash
python manage.py runserver
```

API:

```text
http://127.0.0.1:8000/
```

## API Endpoints

### Authentication

```text
POST /api/auth/register/
POST /api/auth/token/
POST /api/auth/token/refresh/
```

### Expenses

```text
GET    /api/expenses/
POST   /api/expenses/
GET    /api/expenses/<id>/
PATCH  /api/expenses/<id>/
DELETE /api/expenses/<id>/
```

### Filtering

```text
GET /api/expenses/?period=week
GET /api/expenses/?period=month
GET /api/expenses/?period=3months
GET /api/expenses/?start_date=2026-08-01&end_date=2026-08-27
```

## Testing

Run the test suite with:

```bash
python manage.py test
```

## Database

ExpenseFlow uses MySQL, with each expense associated with an authenticated user. Users can only access and manage their own expenses.

## Future Improvements

* Expense categories
* Expense summaries and statistics
* Pagination
* API documentation with Swagger/OpenAPI
* Production deployment

---

Built as a backend project to practice Django REST Framework, JWT authentication, MySQL, and API development.

```

This is the version I'd use. It retains the **professional feel of the longer README** while cutting out the unnecessary explanations.
```
