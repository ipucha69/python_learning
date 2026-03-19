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
# DATABASE_URL = "External Database URL: postgresql://postgress:u9esmFaiJIXzgxKXgr2AN4sHQ8TpL87Y@dpg-d6tqvg3uibrs73enehrg-a.oregon-postgres.render.com/fastapi_db_tvir"

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()