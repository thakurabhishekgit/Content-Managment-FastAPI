from db.database import database, user_collection
from datetime import datetime
from bson import ObjectId
from bson.errors import InvalidId

collab_collection = database.get_collection("collabs")


def serialize_collab(collab):
    return {
        "id": str(collab["_id"]),
        "title": collab["title"],
        "description": collab["description"],
        "owner_id": str(collab["owner_id"]),
        "req_collabs": [str(u) for u in collab["req_collabs"]],
        "created_at": collab["created_at"],
        "updated_at": collab["updated_at"],
    }


def validate_object_id(id: str):
    try:
        return ObjectId(id)
    except InvalidId:
        return None


async def create_collab(data: dict):
    data["owner_id"] = ObjectId(data["owner_id"])
    data["req_collabs"] = []

    data["created_at"] = datetime.utcnow()
    data["updated_at"] = datetime.utcnow()

    result = await collab_collection.insert_one(data)
    new_collab = await collab_collection.find_one({"_id": result.inserted_id})

    return serialize_collab(new_collab)


async def get_all_collabs():
    collabs = []
    async for collab in collab_collection.find():
        collabs.append(serialize_collab(collab))
    return collabs

async def get_collab_by_id(collab_id: str):
    obj_id = validate_object_id(collab_id)
    if not obj_id:
        return None

    collab = await collab_collection.find_one({"_id": obj_id})
    if not collab:
        return None

    return serialize_collab(collab)


async def get_collabs_by_user(user_id: str):
    obj_id = validate_object_id(user_id)
    if not obj_id:
        return []

    collabs = []
    async for collab in collab_collection.find({"owner_id": obj_id}):
        collabs.append(serialize_collab(collab))

    return collabs


async def request_collab(collab_id: str, user_id: str):
    collab_obj = validate_object_id(collab_id)
    user_obj = validate_object_id(user_id)

    if not collab_obj or not user_obj:
        return None

    # check user exists
    user = await user_collection.find_one({"_id": user_obj})
    if not user:
        return None

    await collab_collection.update_one(
        {"_id": collab_obj},
        {"$addToSet": {"req_collabs": user_obj}}
    )

    updated = await collab_collection.find_one({"_id": collab_obj})
    return serialize_collab(updated)