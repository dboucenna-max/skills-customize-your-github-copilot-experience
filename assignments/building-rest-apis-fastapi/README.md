# 🔌 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a simple, well-structured REST API using the FastAPI framework, including defining routes, request/response models, and running the app with Uvicorn.

## 📝 Tasks

### 🛠️ Implement a Todo REST API

#### Description

Create a small REST API for managing a list of Todo items. Implement the API in `starter-code.py` inside this folder. The API should provide endpoints to create, read, update, and delete todos, and should use Pydantic models for request and response validation.

#### Requirements

Completed program should:

- Use `FastAPI` and `Pydantic` models for request/response validation.
- Expose the following endpoints:
  - `GET /todos` — return all todos
  - `GET /todos/{id}` — return a single todo by id (404 if not found)
  - `POST /todos` — create a new todo (return 201 with created item)
  - `PUT /todos/{id}` — update an existing todo (404 if not found)
  - `DELETE /todos/{id}` — delete a todo (404 if not found)
- Store data in-memory (a Python dict or list) so the app can run without a database.
- Include clear example requests and responses in the README.
- Include instructions to run the app locally using `uvicorn`.

### ✨ Optional Enhancements

- Add query parameters for filtering/completeness (e.g., `?completed=true`).
- Add simple validation (title min length) or use UUIDs for ids.
- Add automated tests using `pytest` and `httpx`.

#### Example requests

Create a todo:

```bash
curl -s -X POST "http://127.0.0.1:8000/todos" \
  -H "Content-Type: application/json" \
  -d '{"title":"Buy milk","completed":false}' | jq
```

List todos:

```bash
curl -s "http://127.0.0.1:8000/todos" | jq
```

Run the app locally:

```bash
pip install -r requirements.txt
uvicorn starter-code:app --reload
```

Starter code: `starter-code.py` (edit and run from this folder).

Good luck — build a clean API and try the optional tests if you have time!
