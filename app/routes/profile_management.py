from fastapi import APIRouter

router = APIRouter()

@router.get("/profile-management/")
async def profile_management():
    return {"message": "This is an endpoint for prfoile management."}
