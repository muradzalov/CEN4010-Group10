from sqlalchemy import Column, Integer, String, Float, ForeignKey
from .dependencies import Base
from sqlalchemy.orm import relationship

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

class ShoppingCart(Base):
    __tablename__ = "shopping_cart"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="shopping_cart")
    items = relationship("CartItem", back_populates="cart")

class CartItem(Base):
    __tablename__ = "cart_items"

    id = Column(Integer, primary_key=True, index=True)
    cart_id = Column(Integer, ForeignKey("shopping_cart.id"))
    book_id = Column(Integer, ForeignKey("books.id"))
    quantity = Column(Integer, default=1)

    cart = relationship("ShoppingCart", back_populates="items")
    book = relationship("Book")

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    shopping_cart = relationship("ShoppingCart", back_populates="user", uselist=False)
