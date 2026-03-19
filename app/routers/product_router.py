from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.db import get_db
from app.schemas.product_schema import ProductCreate
from app.services.product_service import get_products, create_product
from app.services.product_service import update_product, delete_product

router = APIRouter(prefix="/products", tags=["products"])

@router.get("/products")
def fetch_products(db: Session = Depends(get_db)):
    return get_products(db)

@router.post("/products")
def add_product(product: ProductCreate, db: Session = Depends(get_db)):
    return create_product(product, db)

@router.put("/{product_id}")
def edit(product_id: int, product: ProductCreate, db: Session = Depends(get_db)):
    return update_product(product_id, product, db)

@router.delete("/{product_id}")
def remove_product(product_id: int, db: Session = Depends(get_db)):
    return delete_product(product_id, db)