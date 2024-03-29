from fastapi import APIRouter
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import date
from ..dependencies import get_db
from ..models import Book
from ..models import User
from ..schemas import Book as BookSchema

router = APIRouter()

# Adds a rating to a particular book
@router.post("/book-ratings/rate/{user_id}")
async def rate_book(user_id: int, book_id: int, rating: float, db: Session = Depends(get_db)):
    if rating > 5 or rating < 0:
        raise HTTPException(status_code=404, detail="Invalid Rating.")
    user = db.query(User).filter(User.id == user_id).first()
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book or not user:
        raise HTTPException(status_code=404, detail="No book or user found with the provided ids.")
    allRatings = [] if not book.rating_list else book.rating_list
    grossRating = 0.0 if not book.rating else book.rating * len(allRatings)
    grossRating += rating
    datestamp = date.today()
    dateString = datestamp.strftime("%Y-%m-%d")
    newRating = {
        "user_id": user.id,
        "user_name": user.name,
        "rating": rating,
        "date": dateString
    }
    allRatings.append(newRating)
    grossRating /= len(allRatings)
    db.query(Book).filter(Book.id == book_id).update({Book.rating: grossRating, Book.rating_list: allRatings}, synchronize_session=False)
    db.commit()
    return {"message": "Rating Added!"}

# Adds a comment to a particular book
@router.post("/book-ratings/comment/{user_id}")
async def comment_on_book(user_id: int, book_id: int, comment: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book or not user:
        raise HTTPException(status_code=404, detail="No book or user found with the provided ids.")
    commentList = [] if not book.comment_list else book.comment_list
    datestamp = date.today()
    dateString = datestamp.strftime("%Y-%m-%d")
    newComment = {
        "user_id": user_id,
        "user_name": user.name,
        "book_title": book.title,
        "date": dateString,
        "comment": comment
    }
    commentList.append(newComment)
    db.query(Book).filter(Book.id == book_id).update({Book.comment_list: commentList}, synchronize_session=False)
    db.commit()
    return {"message": "Comment Added!"}

# Retrieves a list of all comments for a particular book
@router.get("/book-ratings/list-comments/{book_id}")
async def get_all_comments(book_id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="No book was found with the provided id.")
    if not book.comment_list:
        return {"message": f"{book.title} hasn't recieved any comments."}
    return book.comment_list

# Retrieves average rating for a particular book
@router.get("/book-ratings/average-rating/{book_id}")
async def get_average_book_rating(book_id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="No book was found with the provided id.")
    if not book.rating:
        return {"message": f"{book.title} hasn't been rated yet."}
    return {"message": f"Average Rating of {book.title} is {book.rating} stars."}