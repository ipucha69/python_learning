# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, declarative_base

# DATABASE_URL = "postgresql://postgres:password@localhost:5432/fastapi_db"

# engine = create_engine(DATABASE_URL)

# sessionLocal = sessionmaker(bind=engine)

# Base = declarative_base()


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# DATABASE_URL = "sqlite:///./fastapi.db"
# DATABASE_URL = "postgresql://postgres:Ipucha69@localhost:5432/fastapi_db"
DATABASE_URL = "postgresql://root:xN8QuOH7RGLuKmfT133cYfMLmKgR5T1n@dpg-d6ufoa6uk2gs739bf580-a.oregon-postgres.render.com/fastapi_db_035q"

# DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()