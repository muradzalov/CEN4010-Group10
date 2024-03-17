from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..dependencies import get_db
from ..models import ShoppingCart as ShoppingCartModel, CartItem as CartItemModel, Book as BookModel, User as UserModel
from ..schemas import ShoppingCart as ShoppingCartSchema, CartItem as CartItemSchema

router = APIRouter()

@router.post("/shopping-cart/{user_id}/add", response_model=ShoppingCartSchema)
async def add_book_to_cart(user_id: int, item: CartItemSchema, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.user_id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    cart = db.query(ShoppingCartModel).filter(ShoppingCartModel.user_id == user.user_id).first()
    if not cart:
        cart = ShoppingCartModel(user_id=user.user_id)
        db.add(cart)
        db.commit()
        db.refresh(cart)

    book = db.query(BookModel).filter(BookModel.id == item.book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    cart_item = CartItemModel(cart_id=cart.cart_id, book_id=book.id, quantity=item.quantity)
    db.add(cart_item)
    db.commit()
    db.refresh(cart_item)

    return cart

@router.get("/shopping-cart/{user_id}/subtotal", response_model=float)
async def get_cart_subtotal(user_id: int, db: Session = Depends(get_db)):
    cart = db.query(ShoppingCartModel).filter(ShoppingCartModel.user_id == user_id).first()
    if not cart:
        raise HTTPException(status_code=404, detail="Shopping cart not found")

    subtotal = sum(item.quantity * item.book.price for item in cart.cart_items)
    return subtotal

@router.get("/shopping-cart/{user_id}/items", response_model=List[CartItemSchema])
async def get_cart_items(user_id: int, db: Session = Depends(get_db)):
    cart = db.query(ShoppingCartModel).filter(ShoppingCartModel.user_id == user_id).first()
    if not cart:
        raise HTTPException(status_code=404, detail="Shopping cart not found")

    return cart.cart_items

@router.delete("/shopping-cart/{user_id}/remove/{item_id}", response_model=ShoppingCartSchema)
async def remove_book_from_cart(user_id: int, item_id: int, db: Session = Depends(get_db)):
    cart = db.query(ShoppingCartModel).filter(ShoppingCartModel.user_id == user_id).first()
    if not cart:
        raise HTTPException(status_code=404, detail="Shopping cart not found")

    item = db.query(CartItemModel).filter(CartItemModel.item_id == item_id, CartItemModel.cart_id == cart.cart_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Cart item not found")

    db.delete(item)
    db.commit()

    return cart
