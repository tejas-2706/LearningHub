from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy import select # Keep select import for future use
from schemas import Item
from db_config import get_db
from models import DBItem

router = APIRouter(
    prefix='',
    tags=['items']
)


@router.post('/items')
async def create_item(item:Item, db:Session = Depends(get_db)): # query string in url path
    # db = session()
    new_item = DBItem(**item.model_dump())
    db.add(new_item)

    db.commit()
    db.refresh(new_item)

    # db.close()
    # items.append(item)
    return new_item

@router.get('/items', response_model=list[Item])
def list_item(limit:int = 10, db:Session = Depends(get_db)):
    # db = session()

    db_items = db.query(DBItem).order_by(DBItem.id).limit(limit).all()

    # or
# version 2.0 - modern way
    # stmt = select(DBItem).order_by(DBItem.id).limit(limit)
    # db_items = db.execute(stmt).scalars().all()


    # db.close()
    # return items[0:limit]
    return db_items


@router.get('/items/{item_id}', response_model=Item)
def get_item(item_id:int, db:Session = Depends(get_db)) -> Item:
    db_item = db.query(DBItem).filter(DBItem.id == item_id).first()
    # if item_id < len(items):
    #     item = items[item_id]
    #     return item
    if db_item:
        return db_item
    else:
        raise HTTPException(status_code=404, detail="Item Not Found")


@router.put('/items')
def update_item(item_id: int, item:Item ,db:Session = Depends(get_db)):
    try:
        db_item = db.query(DBItem).filter(DBItem.id == item_id).first()
        if db_item:
            db_item.text = item.text
            db_item.is_done = item.is_done
            db.commit()
            db.refresh(db_item)
            return db_item
        else:
            return "No item with the {item_id}"
    except:
        raise HTTPException(status_code=400, detail="Something Went Wrong !!")


@router.delete('/items')
def delete_item(item_id: int, db: Session = Depends(get_db)):
    try:
        db_item = db.query(DBItem).filter(DBItem.id == item_id).first()
        if db_item:
            db.delete(db_item)
            db.commit()
            return "Successfully Deleted"
        else:
            return "No item with the {item_id}"
    except:
        raise HTTPException(status_code=404, detail="Item Not Found")

