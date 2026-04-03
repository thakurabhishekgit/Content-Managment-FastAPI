from motor.motor_asyncio import AsyncIOMotorClient
from core.config import MONGO_URI, DB_NAME

client = AsyncIOMotorClient(MONGO_URI)
database = client[DB_NAME]

# Collections
user_collection = database.get_collection("users")
content_collection = database.get_collection("contents")


# “FastAPI uses async/await to enable non-blocking I/O operations. For database operations, I used Motor, which is an asynchronous MongoDB driver. This allows handling multiple concurrent requests efficiently without blocking the server.”