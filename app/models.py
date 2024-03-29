from sqlalchemy import Column, Integer, String, Float, JSON, ARRAY
from .dependencies import Base

# SQLAlchemy model for the "books" table
class Book(Base):
    __tablename__ = "books"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String, index=True)
    genre = Column(String, index=True)
    rating = Column(Float)
    rating_list = Column(ARRAY(JSON))
    copies_sold = Column(Integer)
    price = Column(Float)
    publisher = Column(String, index=True)
    comment_list = Column(ARRAY(JSON))

# SQLAlchemy model for the "users" table
class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    password = Column(String, index=True)
    name = Column(String, index=True)
    email = Column(String, index=True)
    address = Column(String, index=True)
