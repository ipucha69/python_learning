from app.models.product_model import Product

def get_products(db):
    # db = sessionLocal()
    products = db.query(Product).all()
    db.close()
    return products


def create_product(product_data, db):
    # db = sessionLocal()
    product = Product(
        product_name = product_data.product_name,
        product_desc = product_data.product_desc,
        product_price = product_data.product_price,
        product_quantity = product_data.product_quantity
    )

    db.add(product)
    db.commit()
    db.refresh(product)
    # db.close()
    return product


def update_product(product_id, product_data, db):
    # db = sessionLocal()
    product = db.query(Product).filter(Product.id == product_id).first()

    if not product:
        db.close()
        return None
    
    product.product_name = product_data.product_name
    product.product_desc = product_data.product_desc
    product.product_price = product_data.product_price
    product.product_quantity = product_data.product_quantity

    db.commit()
    db.refresh(product)
    # db.close()
    return product


def delete_product(product_id, db):
    # db = sessionLocal()
    product = db.query(Product).filter(Product.id == product_id).first()

    if not product:
        db.close()
        return None
    
    db.delete(product)
    db.commit()
    # db.close()
    return {"message": "Product deleted successfully"}