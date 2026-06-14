from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List
from fastapi.responses import JSONResponse

app = FastAPI(title="Todo API - Starter")

class TodoIn(BaseModel):
    title: str
    completed: Optional[bool] = False

class TodoOut(TodoIn):
    id: int

# Simple in-memory store
_todos = {}
_next_id = 1

@app.get("/todos", response_model=List[TodoOut])
def list_todos():
    return list(_todos.values())

@app.get("/todos/{todo_id}", response_model=TodoOut)
def get_todo(todo_id: int):
    todo = _todos.get(todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@app.post("/todos", status_code=201, response_model=TodoOut)
def create_todo(payload: TodoIn):
    global _next_id
    todo = payload.dict()
    todo_id = _next_id
    _next_id += 1
    todo_out = {"id": todo_id, **todo}
    _todos[todo_id] = todo_out
    return JSONResponse(status_code=201, content=todo_out)

@app.put("/todos/{todo_id}", response_model=TodoOut)
def update_todo(todo_id: int, payload: TodoIn):
    if todo_id not in _todos:
        raise HTTPException(status_code=404, detail="Todo not found")
    todo = {"id": todo_id, **payload.dict()}
    _todos[todo_id] = todo
    return todo

@app.delete("/todos/{todo_id}", status_code=204)
def delete_todo(todo_id: int):
    if todo_id not in _todos:
        raise HTTPException(status_code=404, detail="Todo not found")
    del _todos[todo_id]
    return JSONResponse(status_code=204, content=None)
