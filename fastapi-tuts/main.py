from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    text : str = None
    is_done : bool = False

items = []

@app.get('/')
def root():
    return {"Hello" : "World"}


@app.post('/items')
def create_item(item:Item): # query string in url path
    items.append(item)
    return items

@app.get('/items', response_model=list[Item])
def list_item(limit:int = 10):
    return items[0:limit]


@app.get('/items/{item_id}', response_model=Item)
def get_item(item_id:int) -> Item:
    if item_id < len(items):
        item = items[item_id]
        return item
    else:
        raise HTTPException(status_code=404, detail="Item Not Found")




