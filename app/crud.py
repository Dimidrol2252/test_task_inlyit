from fastapi import HTTPException
from sqlalchemy.orm import Session
from . import models

def add_item_to_cart(db: Session, user_id: int, item_id: int, quantity: int):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail=f"User with id {user_id} not found")
    
    item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail=f"Item with id {item_id} not found")
    
    if quantity <= 0:
        raise HTTPException(status_code=400, detail="Quantity must be greater than 0")
    
    cart_item = db.query(models.Cart).filter_by(user_id=user_id, item_id=item_id).first()
    if cart_item:
        cart_item.quantity += quantity
    else:
        cart_item = models.Cart(user_id=user_id, item_id=item_id, quantity=quantity)
        db.add(cart_item)
    db.commit()
    db.refresh(cart_item)
    return cart_item

def remove_item_from_cart(db: Session, user_id: int, item_id: int):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail=f"User with id {user_id} not found")

    item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail=f"Item with id {item_id} not found")
    
    cart_item = db.query(models.Cart).filter_by(user_id=user_id, item_id=item_id).first()
    if not cart_item:
        raise HTTPException(status_code=404, detail="Item not found in user's cart")
    
    db.delete(cart_item)
    db.commit()
    return {"detail": "Item removed from cart"}

def update_item_quantity(db: Session, user_id: int, item_id: int, quantity: int):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail=f"User with id {user_id} not found")

    item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail=f"Item with id {item_id} not found")
    
    if quantity <= 0:
        raise HTTPException(status_code=400, detail="Quantity must be greater than 0")

    cart_item = db.query(models.Cart).filter_by(user_id=user_id, item_id=item_id).first()
    if not cart_item:
        raise HTTPException(status_code=404, detail="Item not found in user's cart")
    
    cart_item.quantity = quantity
    db.commit()
    db.refresh(cart_item)
    return cart_item
