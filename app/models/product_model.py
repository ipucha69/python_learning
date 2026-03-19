from sqlalchemy import Column, Integer, String
from app.database.db import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String, nullable=False)
    product_desc = Column(String)
    product_price = Column(Integer)
    product_quantity = Column(Integer)