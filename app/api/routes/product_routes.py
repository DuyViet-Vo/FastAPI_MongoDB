from fastapi import APIRouter, HTTPException
from bson import ObjectId
from app.db.database import products_collection
from app.schemas.product_schemas import ProductSchema
from typing import List

router = APIRouter()


@router.get("/products", response_model=List[ProductSchema])
async def get_products():
    products = await products_collection.find().to_list(100)
    for product in products:
        product["id"] = str(product["_id"])
        del product["_id"]
    return products


@router.get("/products/{product_id}", response_model=ProductSchema)
async def get_product(product_id: str):
    product = await products_collection.find_one({"_id": ObjectId(product_id)})
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    product["id"] = str(product["_id"])
    del product["_id"]
    return product


@router.post("/products", response_model=ProductSchema)
async def create_product(product: ProductSchema):
    new_product = product.dict()
    result = await products_collection.insert_one(new_product)
    new_product["id"] = str(result.inserted_id)
    return new_product


@router.put("/products/{product_id}", response_model=ProductSchema)
async def update_product(product_id: str, product: ProductSchema):
    updated = await products_collection.find_one_and_update(
        {"_id": ObjectId(product_id)}, {"$set": product.dict()}, return_document=True
    )
    if not updated:
        raise HTTPException(status_code=404, detail="Product not found")
    updated["id"] = str(updated["_id"])
    del updated["_id"]
    return updated


@router.delete("/products/{product_id}")
async def delete_product(product_id: str):
    result = await products_collection.delete_one({"_id": ObjectId(product_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Product deleted successfully"}
