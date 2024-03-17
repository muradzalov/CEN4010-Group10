from pydantic import BaseModel
from typing import List, Optional

# Pydantic models for data validation
class BookBase(BaseModel):
    title: str
    author: str
    genre: str
    rating: float
    copies_sold: int
    price: float
    publisher: str

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    username: str
    email: str
    home_address: Optional[str] = None

class UserCreate(UserBase):
    password: str

class User(UserBase):
    user_id: int

    class Config:
        orm_mode = True

class CartItemBase(BaseModel):
    book_id: int
    quantity: int

class CartItemCreate(CartItemBase):
    pass

class CartItem(CartItemBase):
    item_id: int
    cart_id: int

    class Config:
        orm_mode = True

class ShoppingCartBase(BaseModel):
    user_id: int

class ShoppingCartCreate(ShoppingCartBase):
    pass

class ShoppingCart(ShoppingCartBase):
    cart_id: int
    items: List[CartItem] = []

    class Config:
        orm_mode = True