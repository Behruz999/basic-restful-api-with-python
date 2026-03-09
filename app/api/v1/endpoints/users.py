from fastapi import APIRouter, Depends

from app.api.deps import get_user_service
from app.api.v1.schemas.user import UserCreate, UserRead, UserUpdate
from app.services.user_service import UserService

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", response_model=UserRead)
async def create_user(
    payload: UserCreate,
    service: UserService = Depends(get_user_service),
):
    user = await service.create_user(payload.email, payload.password)
    return user


@router.get("/", response_model=list[UserRead])
async def list_users(
    skip: int = 0,
    limit: int = 100,
    service: UserService = Depends(get_user_service),
):
    users = await service.list_users(skip, limit)
    return users


@router.get("/{user_id}", response_model=UserRead)
async def get_user(
    user_id: int,
    service: UserService = Depends(get_user_service),
):
    user = await service.get_user(user_id)
    return user


@router.patch("/{user_id}", response_model=UserRead)
async def update_user(
    user_id: int,
    payload: UserUpdate,
    service: UserService = Depends(get_user_service),
):
    user = await service.update_user(
        user_id,
        payload.email,
        payload.password,
    )
    return user


@router.delete("/{user_id}")
async def delete_user(
    user_id: int,
    service: UserService = Depends(get_user_service),
):
    await service.delete_user(user_id)
    return {"detail": "User deleted"}
