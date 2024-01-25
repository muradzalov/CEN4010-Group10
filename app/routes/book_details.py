from fastapi import APIRouter

router = APIRouter()

@router.get("/book-details/")
async def book_details():
    return {"message": "This is an endpoint for book details."}
