from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, Dict
import uvicorn


class ItemCreate(BaseModel):
    name: str
    description: Optional[str] = None


class Item(ItemCreate):
    id: int


app = FastAPI(title="FastAPI Starter - Assignment")


# In-memory storage
_items: Dict[int, Item] = {}
_next_id = 1


@app.post("/items", response_model=Item, status_code=201)
def create_item(payload: ItemCreate):
    global _next_id
    item = Item(id=_next_id, **payload.dict())
    _items[_next_id] = item
    _next_id += 1
    return item


@app.get("/items", response_model=list[Item])
def list_items():
    return list(_items.values())


@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    item = _items.get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, payload: ItemCreate):
    item = _items.get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    updated = Item(id=item_id, **payload.dict())
    _items[item_id] = updated
    return updated


@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    if item_id not in _items:
        raise HTTPException(status_code=404, detail="Item not found")
    del _items[item_id]
    return None


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
