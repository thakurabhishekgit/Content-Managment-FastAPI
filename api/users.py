
from services.user_service import (
    create_user,
    get_all_users,
    update_user,
    delete_user
)
from fastapi import APIRouter, status
from schemas.user_schema import UserCreate, UserUpdate

router = APIRouter(prefix = "/users" , tags = ["users"])

@router.post("/createUser")
async def createUser(data : dict):
    user = await create_user(data)
    return {
        "status" : True,
        "status_code" : status.HTTP_201_CREATED,
        "message" : "User created successfully",
        "data" : user
    }

@router.get("/getAllUsers")
async def getAllUsers():
    users = await get_all_users()
    return {
        "status" : True,
        "status_code" : status.HTTP_200_OK,
        "message" : "Users fetched successfully",
        "data" : users
    }

@router.put("/updateUser/{user_id}")
async def updateUser(user_id : str , data : dict):
    updated_user = await update_user(user_id , data)
    return {
        "status" : True,
        "status_code" : status.HTTP_200_OK,
        "message" : "User updated successfully",
        "data" : updated_user
    }

@router.delete("/deleteUser/{user_id}")
async def deleteUser(user_id : str):
    deleted_user = await delete_user(user_id)
    return {
        "status" : True,
        "status_code" : status.HTTP_200_OK,
        "message" : "User deleted successfully",
        "data" : deleted_user
    }