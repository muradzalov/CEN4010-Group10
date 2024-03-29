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


# SQLAlchemy model for the "profile" table
class Profile(Base):
    __tablename__ = "profiles"

    pusername = Column(String, index=True)
    pname = Column(String, index=True)
    pemail = Column(String, index=True)
    paddress = Column(String, index=True)
    ppassword = Column(String, primary_key=True, index=True)


class CreditCard(Base):
    __tablename__ = "creditcard"

    cusername = Column(String, index=True)
    ccreditcard = Column(Integer, primary_key=True)
    csc = Column(Integer)
    czipcode = Column(Integer)
    cexpdate = Column(Integer)
