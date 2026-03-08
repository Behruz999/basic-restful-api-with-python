from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.api.v1.schemas.user import UserCreate, UserRead
from app.services.user_service import UserService
from app.repositories.user_repo import UserRepository

# router = APIRouter()
router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", response_model=UserRead)
def create_user(
    payload: UserCreate,
    db: Session = Depends(get_db),
):
    repo = UserRepository(db)
    service = UserService(repo)

    user = service.create_user(email=payload.email, password=payload.password)

    return user
