from fastapi import APIRouter, status
from schemas.content_schema import ContentCreate, ContentUpdate
from services.content_service import (
    create_content,
    get_all_contents,
    update_content,
    delete_content
)

router = APIRouter(prefix="/content", tags=["Content"])

@router.post("/")
async def create(data: ContentCreate):
    content = await create_content(data.dict())

    return {
        "status": True,
        "status_code": status.HTTP_201_CREATED,
        "message": "Content created successfully",
        "data": content
    }


@router.get("/")
async def get_all():
    contents = await get_all_contents()

    return {
        "status": True,
        "status_code": status.HTTP_200_OK,
        "message": "Contents fetched successfully",
        "data": contents
    }


@router.put("/{content_id}")
async def update(content_id: str, data: ContentUpdate):
    updated = await update_content(content_id, data.dict(exclude_unset=True))

    return {
        "status": True,
        "status_code": status.HTTP_200_OK,
        "message": "Content updated successfully",
        "data": updated
    }


@router.delete("/{content_id}")
async def delete(content_id: str):
    await delete_content(content_id)

    return {
        "status": True,
        "status_code": status.HTTP_200_OK,
        "message": "Content deleted successfully",
        "data": {}
    }

