from fastapi import APIRouter, HTTPException
from datetime import datetime
from random import randint
from typing import Any

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

router = APIRouter(
    prefix='',
    tags=["Campaigns"]
)



@router.get('/campaigns')
async def read_campaigns():
    return {"campaigns":data}

@router.get('/campaigns/{id}')
async def read_campaign(id : int):
    for campaign in data:
        if campaign.get("campaign_id") == id:
            return campaign
    raise HTTPException(status_code=404) 

@router.post('/campaigns')
async def create_campaign(body:dict[str,Any]):
    new:Any = {
        "campaign_id": randint(100,1000),
        "name": body.get("name"),
        "due_date": body.get("due_date"),
        "created_at":datetime.now()
    }

    data.append(new)
    return {"campaign" : new}

@router.delete('/campaigns/{id}')
async def delete_campaign(id : int):
    for index, campaign in enumerate(data):
        if campaign.get("campaign_id") == id:
            data.pop(index)
            return {"message": "Campaign deleted successfully"}

    raise HTTPException(status_code=404, detail=f"Campaign with ID {id} not found")
