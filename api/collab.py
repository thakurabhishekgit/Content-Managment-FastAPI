from fastapi import APIRouter, status
from schemas.collab_schema import CollabCreate
from services.collab_service import (
    create_collab,
    get_all_collabs,
    get_collab_by_id,
    get_collabs_by_user,
    request_collab
)

router = APIRouter(prefix="/collab", tags=["Collab"])


@router.post("/")
async def create(data: CollabCreate):
    collab = await create_collab(data.dict())

    return {
        "status": True,
        "status_code": status.HTTP_201_CREATED,
        "message": "Collab created successfully",
        "data": collab
    }


@router.post("/")
async def create(data: CollabCreate):
    collab = await create_collab(data.dict())

    return {
        "status": True,
        "status_code": status.HTTP_201_CREATED,
        "message": "Collab created successfully",
        "data": collab
    }


@router.get("/{collab_id}")
async def get_by_id(collab_id: str):
    collab = await get_collab_by_id(collab_id)

    if not collab:
        return {
            "status": False,
            "status_code": 404,
            "message": "Collab not found",
            "data": {}
        }

    return {
        "status": True,
        "status_code": 200,
        "message": "Collab fetched",
        "data": collab
    }


@router.get("/{collab_id}")
async def get_by_id(collab_id: str):
    collab = await get_collab_by_id(collab_id)

    if not collab:
        return {
            "status": False,
            "status_code": 404,
            "message": "Collab not found",
            "data": {}
        }

    return {
        "status": True,
        "status_code": 200,
        "message": "Collab fetched",
        "data": collab
    }           

@router.post("/{collab_id}/request/{user_id}")
async def request(collab_id: str, user_id: str):
    collab = await request_collab(collab_id, user_id)

    if not collab:
        return {
            "status": False,
            "status_code": 400,
            "message": "Invalid collab or user",
            "data": {}
        }

    return {
        "status": True,
        "status_code": 200,
        "message": "Request added successfully",
        "data": collab
    }