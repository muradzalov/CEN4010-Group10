from fastapi import APIRouter

router = APIRouter()

@router.get("/shopping-cart/")
async def shopping_cart():
    return {"message": "This is an endpoint for the shopping cart."}
