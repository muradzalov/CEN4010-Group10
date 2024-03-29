from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..dependencies import get_db
from ..models import ShoppingCart as ShoppingCartModel, CartItem as CartItemModel, Book as BookModel, User as UserModel
from ..schemas import ShoppingCart as ShoppingCartSchema, CartItem

router = APIRouter()

# Functionality: Retrieve the subtotal price of all items in the user’s shopping cart
    # Logic: Given a user Id, return the subtotal of the books in the cart
    # HTTP Request Type: GET
    # Parameters Sent: User Id
    # Response Data: Calculated Subtotal
@router.get("/shopping-cart/{user_id}/subtotal", response_model=float)
async def get_cart_subtotal(user_id: int, db: Session = Depends(get_db)):
    cart = db.query(ShoppingCartModel).filter(ShoppingCartModel.user_id == user_id).first()
    if not cart:
        raise HTTPException(status_code=404, detail="Shopping cart not found")

    subtotal = sum(item.quantity * item.book.price for item in cart.cart_items)
    return subtotal

# Functionality: Add a book to the shopping cart
    # Logic: Provided with a book Id and a User Id, add the book to the user’s shopping cart
    # HTTP Request Type: POST
    # Parameters Sent: Book Id, User Id
    # Response Data: None
@router.post("/shopping-cart/{user_id}/add", response_model=None)
async def add_book_to_cart(user_id: int, book_id: int, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.user_id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    cart = db.query(ShoppingCartModel).filter(ShoppingCartModel.user_id == user.user_id).first()
    if not cart:
        cart = ShoppingCartModel(user_id=user.user_id)
        db.add(cart)
        db.commit()
        db.refresh(cart)

    book = db.query(BookModel).filter(BookModel.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    cart_item = CartItemModel(cart_id=cart.cart_id, book_id=book.id, quantity=1)  # Default quantity to 1
    db.add(cart_item)
    db.commit()

# Functionality: Retrieve the list of books in the user’s shopping cart
    # Logic: Given a user Id, return a list of books that are in the shopping cart
    # HTTP Request Type: GET
    # Parameters Sent: User Id
    # Response Data: List of Book Objects
    
@router.get("/shopping-cart/{user_id}/items", response_model=List[dict])
async def get_cart_items(user_id: int, db: Session = Depends(get_db)):
    cart = db.query(ShoppingCartModel).filter(ShoppingCartModel.user_id == user_id).first()
    if not cart:
        raise HTTPException(status_code=404, detail="Shopping cart not found")
    
    cart_items = db.query(
        CartItemModel.item_id,
        CartItemModel.quantity,
        BookModel.title,
        BookModel.author,
        BookModel.genre,
        BookModel.price
    ).join(BookModel, CartItemModel.book_id == BookModel.id).filter(CartItemModel.cart_id == cart.cart_id).all()
    result = []
    for item_id, quantity, title, author, genre, price in cart_items:
        item_data = {
            "item_id": item_id,
            "quantity": quantity,
            "book": {
                "title": title,
                "author": author,
                "genre": genre,
                "price": price
            }
        }
        result.append(item_data)

    return result



# Functionality: Delete a book from the shopping cart instance for that user
    # Logic: Given a book Id and a User Id, remove the book from the user’s shopping cart
    # HTTP Request Type: DELETE
    # Parameters Sent: Book Id, User Id
    # Response Data: None
@router.delete("/shopping-cart/{user_id}/remove/{book_id}", response_model=None)
async def remove_book_from_cart(user_id: int, book_id: int, db: Session = Depends(get_db)):
    cart = db.query(ShoppingCartModel).filter(ShoppingCartModel.user_id == user_id).first()
    if not cart:
        raise HTTPException(status_code=404, detail="Shopping cart not found")

    item = db.query(CartItemModel).filter(CartItemModel.book_id == book_id, CartItemModel.cart_id == cart.cart_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Cart item not found")

    db.delete(item)
    db.commit()