from db.database import user_collection
from datetime import datetime
from bson import ObjectId


def serialize_user(user) -> dict:
    return {
        "id": str(user["_id"]),
        "name": user["name"],
        "email": user["email"],
        "created_at": user["created_at"],
        "updated_at": user["updated_at"],
    }


async def create_user(data : dict):
    data["created_at"] = datetime.utcnow()
    data["updated_at"] = datetime.utcnow()


    result = await user_collection.insert_one(data)
    new_user = await user_collection.find_one({"_id" : result.inserted_id})

    return serialize_user(new_user)

async def get_all_users():
    users = []
    async for user in user_collection.find():
        users.append(serialize_user(user))
    return users

async def update_user(user_id : str , data : dict):
    data["updated_at"] = datetime.utcnow()

    await user_collection.find_one_and_update(
        {"_id" : ObjectId(user_id)},
        {"$set" : data}
    )

    updated_user = await user_collection.find_one({"_id" : ObjectId(user_id)})
    return serialize_user(updated_user)



async def delete_user(user_id : str):
    deleted_user = await user_collection.find_one({"_id" : ObjectId(user_id)})
    await user_collection.delete_one({"_id" : ObjectId(user_id)})
    return f"user {user_id} and {deleted_user['name']} deleted successfully"
