from db.database import content_collection
from datetime import datetime
from bson import ObjectId

def serialize_content(content) -> dict:
    return {
        "id": str(content["_id"]),
        "title": content["title"],
        "description": content["description"],
        "tags": content["tags"],
        "created_at": content["created_at"],
        "updated_at": content["updated_at"],
    }

async def create_content(data: dict):
    data["created_at"] = datetime.utcnow()
    data["updated_at"] = datetime.utcnow()

    result = await content_collection.insert_one(data)
    new_content = await content_collection.find_one({"_id": result.inserted_id})
    return serialize_content(new_content)

async def get_all_contents():
    contents = []
    async for content in content_collection.find():
        contents.append(serialize_content(content))
    return contents

async def update_content(content_id: str, data: dict):
    data["updated_at"] = datetime.utcnow()

    await content_collection.update_one(
        {"_id": ObjectId(content_id)},
        {"$set": data}
    )

    updated = await content_collection.find_one({"_id": ObjectId(content_id)})
    return serialize_content(updated)

async def delete_content(content_id: str):
    await content_collection.delete_one({"_id": ObjectId(content_id)})
    return True