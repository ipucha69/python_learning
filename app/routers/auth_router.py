from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.db import get_db
from jose import jwt, JWTError, ExpiredSignatureError
from fastapi.security import OAuth2PasswordBearer
from app.schemas.user_schema import UserResponse
from app.schemas.auth_schema import RegistrationUser, LoginUser
from app.services.auth_service import login_user, create_user
from app.models.user_model import User

SECRET_KEY = "supersecretkey"
ALGORITHM = "HS256"

router = APIRouter(prefix="/auth", tags=["Auth"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

@router.get("/me", response_model=UserResponse)
def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("user_id")

    except ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")

    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

    user = db.query(User).filter(User.id == user_id).first()

    return user

@router.post("/register")
def user_registration(user_data: RegistrationUser, db:Session=Depends(get_db)):
    return create_user(user_data, db)

@router.post("/login")
def user_login(user_data: LoginUser, db:Session=Depends(get_db)):
    return login_user(user_data, db)