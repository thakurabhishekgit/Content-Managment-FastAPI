from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import MONGO_URI, DB_NAME

client = AsyncIOMotorClient(MONGO_URI)
database = client[DB_NAME]

# Collections
user_collection = database.get_collection("users")
content_collection = database.get_collection("contents")