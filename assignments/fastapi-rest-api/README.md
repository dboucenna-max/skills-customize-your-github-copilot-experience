# 🛠️ Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a simple REST API using the FastAPI framework. You'll create endpoints, validate input with Pydantic models, and run the app locally to explore automatic API docs.

## 📝 Tasks

### 🛠️ Create a CRUD API for `Item`

#### Description
Implement a small REST API that manages `Item` resources. The API should allow creating, reading, updating, and deleting items using JSON over HTTP. Use the provided starter code to get started quickly.

#### Requirements
Completed program should:

- Provide endpoints for: create (`POST /items`), list (`GET /items`), retrieve (`GET /items/{id}`), update (`PUT /items/{id}`), and delete (`DELETE /items/{id}`).
- Use Pydantic models for request validation and response serialization.
- Return appropriate HTTP status codes (`201` for create, `404` for not found, etc.).
- Handle invalid input with clear error responses.
- Store data in-memory (dictionary or list) so the API is self-contained for the assignment.
- Expose interactive API docs at `/docs` (FastAPI provides this by default).

### ✨ Optional Enhancements

- Add query parameters for filtering or pagination on `GET /items`.
- Persist items to a simple JSON file between runs.
- Add authentication (API key) for write operations.

#### Example Requests

Create item:

```
POST /items
{
  "name": "Notebook",
  "description": "A small notebook"
}

Response: 201
{
  "id": 1,
  "name": "Notebook",
  "description": "A small notebook"
}
```

List items:

```
GET /items

Response: 200
[
  {"id":1, "name":"Notebook", "description":"A small notebook"}
]
```

Starter code: `starter-code.py` in this folder.

## Run locally

1. Create a virtual environment and install requirements:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Start the app:

```bash
python starter-code.py
```

3. Open the interactive docs at: http://127.0.0.1:8000/docs

Good luck — build a working API and try the optional enhancements when you're ready.
