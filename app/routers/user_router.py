from fastapi import APIRouter, Depends
from app.database.db import get_db
from sqlalchemy.orm import Session
from app.schemas.user_schema import UserCreate
from app.services.user_service import get_users, create_user

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/")
def fetch_users(db: Session = Depends(get_db)):
    return get_users(db)

@router.post("/")
def add_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(user, db)