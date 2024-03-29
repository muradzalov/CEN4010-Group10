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
    password: str
    email: str
    home_address: Optional[str]

class UserCreate(UserBase):
    pass

class User(UserBase):
    user_id: int

    class Config:
        orm_mode = True

class ShoppingCartBase(BaseModel):
    user_id: int

class ShoppingCartCreate(ShoppingCartBase):
    pass

class ShoppingCart(ShoppingCartBase):
    cart_id: int
    user: User

    class Config:
        orm_mode = True

class CartItemBase(BaseModel):
    cart_id: int
    book_id: int
    quantity: int

class CartItemCreate(CartItemBase):
    pass

class CartItem(CartItemBase):
    book_id: int

    class Config:
        orm_mode = True