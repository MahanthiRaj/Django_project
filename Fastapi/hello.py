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



products = {
    1: {"name": "Laptop", "price": 999.99},
    2: {"name": "Phone", "price": 499.99}
}

class Product(BaseModel):
    name: str
    price: float

@app.get("/products")
async def get_all():
    return {"products": products}


@app.post("/products/{product_id}")
async def add_product(product_id: int, product: Product):
    if product_id in products:
        return {"error": "Product ID already exists"}
    products[product_id] = product.dict()
    return {"message": "Product added", "product": product}

@app.put("/products/{product_id}")
async def update_product(product_id: int, product: Product):
    if product_id not in products:
        return {"error": "Product not found"}
    products[product_id] = product.dict()
    return {"message": "Product updated", "product": product}

@app.delete("/products/{product_id}")
async def delete_product(product_id: int):
    if product_id in products:
        deleted = products.pop(product_id)
        return {"message": "Product deleted", "product": deleted}
    return {"error": "Product not found"}

