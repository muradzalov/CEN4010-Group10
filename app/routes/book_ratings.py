from fastapi import APIRouter

router = APIRouter()

@router.get("/book-ratings/")
async def book_ratings():
    return {"message": "This is an endpoint for book ratings."}
