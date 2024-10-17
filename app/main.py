from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, crud
from .database import engine, get_db

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

@app.post("/cart/add/")
async def add_to_cart(user_id: int, item_id: int, quantity: int, db: Session = Depends(get_db)):
    return crud.add_item_to_cart(db, user_id, item_id, quantity)

@app.delete("/cart/remove/")
async def remove_from_cart(user_id: int, item_id: int, db: Session = Depends(get_db)):
    return crud.remove_item_from_cart(db, user_id, item_id)

@app.put("/cart/update/")
async def update_cart(user_id: int, item_id: int, quantity: int, db: Session = Depends(get_db)):
    return crud.update_item_quantity(db, user_id, item_id, quantity)
