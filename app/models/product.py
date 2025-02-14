from pydantic import BaseModel


class ProductModel:
    collection_name = "products"
    name: str
    price: float
    stock: int
