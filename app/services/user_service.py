from app.models.user import User
from app.repositories.user_repo import UserRepository
from app.core.exceptions import NotFoundException, ConflictException


class UserService:

    def __init__(self, repo: UserRepository):
        self.repo = repo

    async def create_user(self, email: str, password: str):

        existing = await self.repo.get_by_email(email)
        if existing:
            raise ConflictException("Email already registered")

        user = User(email=email, password=password)

        return await self.repo.create(user)

    async def get_user(self, user_id: int):

        user = await self.repo.get(user_id)

        if not user:
            raise NotFoundException("User not found")

        return user

    async def list_users(self, skip: int = 0, limit: int = 100):

        return await self.repo.get_all(skip, limit)

    async def update_user(self, user_id: int, email=None, password=None):

        user = await self.repo.get(user_id)

        if not user:
            raise NotFoundException("User not found")

        if email:
            user.email = email

        if password:
            user.password = password

        return await self.repo.update(user)

    async def delete_user(self, user_id: int):

        user = await self.repo.get(user_id)

        if not user:
            raise NotFoundException("User not found")

        await self.repo.delete(user)
