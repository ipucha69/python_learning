from fastapi import HTTPException
from app.models.user_model import User
from app.utils.auth import hash_password, verify_password, create_access_token

def create_user(user_data, db):
    hashed = hash_password(user_data.password)
    user = User(
        name = user_data.name,
        email = user_data.email,
        password = hashed
    )
    
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def login_user(user_data, db):

    user = db.query(User).filter(User.email == user_data.email).first()

    if not user:
        raise HTTPException(status_code=401, detail="Invalid email or password")

    if not verify_password(user_data.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid email or password")

    token = create_access_token({"user_id": user.id})

    return {"access_token": token}