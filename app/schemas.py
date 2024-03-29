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
    name: str
    email: str
    address: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int

    class Config:
        orm_mode = True