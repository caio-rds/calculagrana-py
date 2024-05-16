from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder

from app.src.model.user import CreateUser, UpdateUser, ReadUser
from app.src.controller.user import create, read, update, delete

router = APIRouter()


@router.post("/", response_model=ReadUser)
async def create_user(new_user: CreateUser) -> ReadUser:
    creation = await create(new_user)
    return creation


@router.get("/{username}", response_model=ReadUser, response_model_exclude_unset=True)
async def get_user(username: str, conversions: bool = False) -> ReadUser:
    if user := await read(username, conversions):
        return user
    raise HTTPException(status_code=404, detail="User not found")


@router.put("/", response_model=ReadUser)
async def update_user(user: UpdateUser) -> ReadUser:
    if updated := await update(user):
        return updated
    raise HTTPException(status_code=500, detail="Failed to update user")


@router.delete("/{username}")
async def delete_user(username: str):
    if await delete(username):
        return {
            "status": "success",
            "message": f"User {username} deleted successfully"
        }
    raise HTTPException(status_code=500, detail="Failed to delete user")


@router.put("/reset-password")
async def reset_password(u_id: str):
    pass
    # return await delete(u_id=u_id)
