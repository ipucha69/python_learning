from app.models.user_model import User
from app.database.db import sessionLocal

def get_users(db):
    # db = sessionLocal()
    users = db.query(User).all()
    # db.close()
    return users

def create_user(user_data, db):
    # db = sessionLocal()
    user = User(
        name = user_data.name,
        title = user_data.title
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    # db.close()
    return user
