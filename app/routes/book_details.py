from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..dependencies import get_db
from ..models import Book
from ..schemas import Book as BookSchema

from fastapi import APIRouter

router = APIRouter()

@router.get("/book-details/")
async def book_details():
    return {"message": "This is an endpoint for book details."}
