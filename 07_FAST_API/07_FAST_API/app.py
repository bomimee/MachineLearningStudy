from fastapi import FastAPI
from pydantic import BaseModel
from typing import List


app = FastAPI()

class Item(BaseModel):
    id:int
    name:str
    price: float

items = [
        {"id": 1, "name":"Apple", "price":5000},
        {"id": 2, "name": "Mango", "price": 6000},
        {"id": 3, "name": "Banana", "price": 4500},
    ]
@app.get("/")
def hello():
    return "Hello Fast_API"


@app.get("/items", response_model=List[Item])
def get_items():
    return items

@app.post("/")
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")