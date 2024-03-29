from pydantic import BaseModel, Json
from typing import List

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

class UserBase(BaseModel):
    username: str
    password: str
    name: str
    email: str
    address: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int

    class Config:
        orm_mode = True