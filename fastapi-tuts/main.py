from fastapi import FastAPI,HTTPException
from datetime import datetime
from random import randint
from typing import Any
from schemas import Item
from database import session,engine

import models 
from models import DBItem

app = FastAPI(root_path="/api/v1")

models.Base.metadata.create_all(bind=engine)

items = []

# def init_db():
#     db = session()
#     new_item = DBItem(text="Buy phone", is_done=False)
#     db.add(new_item)
#     db.commit()
#     db.close()

# init_db()


@app.get('/')
async def root():
    return {"messsage" : "Hello, World !!"}


@app.post('/items')
def create_item(item:Item): # query string in url path
    db = session()
    new_item = DBItem(**item.model_dump())
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    db.close()
    # items.append(item)
    return new_item

@app.get('/items', response_model=list[Item])
def list_item(limit:int = 10):
    db = session()
    db_items = db.query(DBItem).limit(limit).all()
    db.close()
    # return items[0:limit]
    return db_items


@app.get('/items/{item_id}', response_model=Item)
def get_item(item_id:int) -> Item:
    if item_id < len(items):
        item = items[item_id]
        return item
    else:
        raise HTTPException(status_code=404, detail="Item Not Found")



data = [
    {
        "campaign_id": 1,
        "name":"Summer Launch",
        "due_date": datetime.now(),
        "created_at":datetime.now()
    },
    {
        "campaign_id": 2,
        "name":"Winter Launch",
        "due_date": datetime.now(),
        "created_at":datetime.now()
    },
    {
        "campaign_id": 3,
        "name":"Rainy Launch",
        "due_date": datetime.now(),
        "created_at":datetime.now()
    }
]


@app.get('/campaigns')
async def read_campaigns():
    return {"campaigns":data}

@app.get('/campaigns/{id}')
async def read_campaign(id : int):
    for campaign in data:
        if campaign.get("campaign_id") == id:
            return campaign
    raise HTTPException(status_code=404) 

@app.post('/campaigns')
async def create_campaign(body:dict[str,Any]):
    new:Any = {
        "campaign_id": randint(100,1000),
        "name": body.get("name"),
        "due_date": body.get("due_date"),
        "created_at":datetime.now()
    }

    data.append(new)
    return {"campaign" : new}

@app.delete('/campaigns/{id}')
async def delete_campaign(id : int):
    for index, campaign in enumerate(data):
        if campaign.get("campaign_id") == id:
            data.pop(index)
            return {"message": "Campaign deleted successfully"}

    raise HTTPException(status_code=404, detail=f"Campaign with ID {id} not found")
