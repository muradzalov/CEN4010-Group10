<<<<<<< HEAD
from pydantic import BaseModel
from typing import List, Optional
=======
from pydantic import BaseModel, Json
from typing import List
>>>>>>> 251d63ef791b4fa4dc91480f5ac827bc30c97cd8

# Pydantic models for data validation
class BookBase(BaseModel):
    title: str
    author: str
    genre: str
    rating: float
    rating_list: List[Json]
    copies_sold: int
    price: float
    publisher: str
    comment_list: List[Json]

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int

    class Config:
        orm_mode = True

class ProfileBase(BaseModel):
    pusername: str
    pname: str
    pemail: str
    paddress: str

class ProfileCreate(ProfileBase):
    pass
class Profile(ProfileBase):
    ppassword: str

    class Config:
        orm_mode = True

class CreditBase(BaseModel):
    cusername: str
    csc: int
    czipcode: int
    cexpdate: str

class CreditCreate(CreditBase):
    pass

class Credit(CreditBase):
    ccreditcard: int
class UserBase(BaseModel):
    username: str
    password: str
<<<<<<< HEAD
    email: str
    home_address: Optional[str]
=======
    name: str
    email: str
    address: str
>>>>>>> 251d63ef791b4fa4dc91480f5ac827bc30c97cd8

class UserCreate(UserBase):
    pass

class User(UserBase):
<<<<<<< HEAD
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
=======
    id: int
>>>>>>> 251d63ef791b4fa4dc91480f5ac827bc30c97cd8

    class Config:
        orm_mode = True