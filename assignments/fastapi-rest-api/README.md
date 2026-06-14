# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API using the FastAPI framework to learn request handling, data validation with Pydantic, and creating OpenAPI-driven documentation.

## 📝 Tasks

### 🛠️ Implement a CRUD API for `Item`

#### Description
Create a FastAPI application that provides endpoints to create, read, update, and delete `Item` resources. Use an in-memory store for simplicity and provide clear JSON request and response formats.

#### Requirements
Completed program should:

- Provide endpoints: `GET /items`, `GET /items/{id}`, `POST /items`, `PUT /items/{id}`, `DELETE /items/{id}`.
- Validate request bodies using Pydantic models and return appropriate status codes (`201` for creation, `404` for missing resources, etc.).
- Return JSON responses and meaningful error messages for invalid data.
- Include minimal inline documentation and run via `uvicorn`.

#### Example request/response

```
POST /items
{
  "name": "Notebook",
  "description": "College ruled",
  "price": 3.5
}

Response 201 Created
{
  "id": 1,
  "name": "Notebook",
  "description": "College ruled",
  "price": 3.5
}
```

#### How to run

From this folder:

```bash
python -m pip install -r requirements.txt
python -m uvicorn starter-code:app --reload --port 8000
```

Open the interactive docs at `http://127.0.0.1:8000/docs`.

### ✨ Optional Enhancements

- Persist items to SQLite using SQLModel or SQLAlchemy.
- Add filtering, pagination, or search to `GET /items`.
- Protect endpoints with simple API key authentication.

Starter code: `starter-code.py` (edit and run from this folder).
