from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#message = "Hello world"

# @app.get("/")
# async def hello():
#     return message

# @app.post("/")
# async def create(new_message: str):
#     global message
#     message = new_message
#     return {"message": message}

# @app.put("/")
# async def update(new_message: str):
#     global message
#     message = new_message
#     return {"message": message}

# @app.delete("/")
# async def delete():
#     global message
#     message = ""
#     return {"message": message}




class Item(BaseModel):
    name: str
    price: float

items = {
    1: {"name": "Example", "price": 9.99}
}

@app.get("/items/{item_id}", response_model=Item)
async def get_item(item_id: int):
    return items[item_id]

@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    return item

@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, item: Item):
    items[item_id] = item.dict()
    return item

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    deleted = items.pop(item_id)
    return {"deleted": deleted}

