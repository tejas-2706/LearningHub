from fastapi import FastAPI
from database import engine
from fastapi.middleware.cors import CORSMiddleware
from routers import campaigns
from routers import items

import models 


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000'],
    allow_methods=['*']
)

models.Base.metadata.create_all(bind=engine)

# items = []

@app.get('/')
async def root():
    return {"messsage" : "Hello, World !!"}


app.include_router(campaigns.router, prefix='/api/v1')
app.include_router(items.router, prefix='/api/v1')

# def init_db():
#     db = session()
#     new_item = DBItem(text="Buy phone", is_done=False)
#     db.add(new_item)
#     db.commit()
#     db.close()

# init_db()

