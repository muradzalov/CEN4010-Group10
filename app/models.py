from sqlalchemy import Column, Integer, String, Float, ForeignKey, Text
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

class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    home_address = Column(Text)

    shopping_carts = relationship('ShoppingCart', back_populates='user')

class ShoppingCart(Base):
    __tablename__ = 'shopping_cart'

    cart_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)

    user = relationship('User', back_populates='shopping_carts')
    cart_items = relationship('CartItem', back_populates='shopping_cart')

class CartItem(Base):
    __tablename__ = 'cart_items'

    item_id = Column(Integer, primary_key=True, index=True)
    cart_id = Column(Integer, ForeignKey('shopping_cart.cart_id'), nullable=False)
    book_id = Column(Integer, ForeignKey('books.id'), nullable=False)  # Refer to 'id' as defined in Book model
    quantity = Column(Integer, nullable=False)

    shopping_cart = relationship('ShoppingCart', back_populates='cart_items')
    book = relationship('Book')