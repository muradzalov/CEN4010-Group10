from sqlalchemy import Column, Integer, String, Float
from .dependencies import Base


# SQLAlchemy model for the "books" table
class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String, index=True)
    genre = Column(String, index=True)
    rating = Column(Float)
    copies_sold = Column(Integer)
    price = Column(Float)
    publisher = Column(String, index=True)