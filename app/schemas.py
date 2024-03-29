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