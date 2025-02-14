from motor.motor_asyncio import AsyncIOMotorClient
from app.models.product import ProductModel

from app.core.config import settings

client = AsyncIOMotorClient(settings.MONGO_URI)
database = client[settings.DATABASE_NAME]
users_collection = database.get_collection("users")
products_collection = database.get_collection(ProductModel.collection_name)
