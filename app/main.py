from fastapi import FastAPI, Depends
from .routes import book_browsing, profile_management, shopping_cart, book_details, book_ratings, wish_list
from .dependencies import get_db
from sqlalchemy.orm import Session
from sqlalchemy import text

app = FastAPI()

# Checks to see if the API is connected to the database
@app.get("/server-db-healthcheck", summary="Status of Server Connection to DB", description="Checks the connection between the server and the database. Returns 'healthy' if the connection is established successfully; otherwise, returns 'unhealthy'.")
def health_check(db: Session = Depends(get_db)):
    try:
        db.execute(text('SELECT 1'))
        return {"status": "healthy"}
    except Exception as e:
        return {"status": "unhealthy", "details": str(e)}

# Routers from each feature
app.include_router(book_browsing.router)
app.include_router(profile_management.router)
app.include_router(shopping_cart.router)
app.include_router(book_details.router)
app.include_router(book_ratings.router)
app.include_router(wish_list.router)
