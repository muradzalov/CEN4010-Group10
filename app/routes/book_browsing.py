from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..dependencies import get_db
from ..models import Book
from ..schemas import Book as BookSchema

router = APIRouter()

# Retrieves list of books by genre
@router.get("/book-browsing/genre/{genre}", response_model=List[BookSchema], summary="Retrieve Books by Genre", description="Fetches a list of books (represented by objects), filtered by the specified genre.")
async def get_books_by_genre(genre: str, db: Session = Depends(get_db)):
    books = db.query(Book).filter(Book.genre == genre).all()
    if not books:
        raise HTTPException(status_code=404, detail="No books found for the specified genre")
    return books

# Retrieve list of top sellers (top 10 books that have sold the most copied)
@router.get("/book-browsing/top-sellers", response_model=List[BookSchema], summary="List Top Selling Books", description="Retrieves a list of the top 10 best-selling books, ordered by the number of copies sold in descending order.")
async def get_top_sellers(db: Session = Depends(get_db)):
    top_sellers = db.query(Book).order_by(Book.copies_sold.desc()).limit(10).all()
    return top_sellers

# Retrieve list of books for a particular rating and higher
@router.get("/book-browsing/rating/{rating}", response_model=List[BookSchema], summary="Find Books by Minimum Rating", description="Returns a list of books that have a rating equal to or higher than the specified value.")
async def get_books_by_rating(rating: float, db: Session = Depends(get_db)):
    books = db.query(Book).filter(Book.rating >= rating).all()
    return books

# Discount books by publisher
@router.put("/book-browsing/discount", summary="Apply Discount to Books by Publisher", description="Updates the price of books published by the specified publisher, applying a given percentage discount.")
async def discount_books_by_publisher(publisher: str, discount: float, db: Session = Depends(get_db)):
    discount_factor = 1 - (discount / 100)
    db.query(Book).filter(Book.publisher == publisher).update({Book.price: Book.price * discount_factor}, synchronize_session=False)
    db.commit()
    return {"message": f"Prices for books from publisher {publisher} have been updated by a discount of {discount}%"}
