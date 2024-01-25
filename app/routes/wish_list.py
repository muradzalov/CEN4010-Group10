from fastapi import APIRouter

router = APIRouter()

@router.get("/wish-list/")
async def wish_list():
    return {"message": "This is an endpoint for the wish list."}
