from pydantic import BaseModel

class ProductCreate(BaseModel):
    product_name: str
    product_desc: str
    product_price: int
    product_quantity: int