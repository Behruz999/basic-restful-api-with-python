from app.models.user import User
from app.repositories.user_repo import UserRepository


class UserService:

    def __init__(self, repo: UserRepository):
        self.repo = repo

    def create_user(self, email: str, password: str):

        existing = self.repo.get_by_email(email)
        if existing:
            raise ValueError("Email already registered")

        user = User(email=email, hashed_password=password)

        return self.repo.create(user)

    def get_user(self, user_id: int):

        user = self.repo.get(user_id)

        if not user:
            raise ValueError("User not found")

        return user

    def list_users(self, skip: int = 0, limit: int = 100):

        return self.repo.get_all(skip, limit)

    def update_user(self, user_id: int, email=None, password=None):

        user = self.repo.get(user_id)

        if not user:
            raise ValueError("User not found")

        if email:
            user.email = email

        if password:
            user.password = password

        return self.repo.update(user)

    def delete_user(self, user_id: int):

        user = self.repo.get(user_id)

        if not user:
            raise ValueError("User not found")

        self.repo.delete(user)
