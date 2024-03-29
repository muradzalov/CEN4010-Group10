from pydantic import BaseModel

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

    class Config:
        orm_mode = True