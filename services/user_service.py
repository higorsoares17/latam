from models.user_model import Users
from fastapi import Depends
from typing import Optional, List
from schemas.user_schema import UserSchema, UserSchemaUpdate
from repositories.user_repository import UserRepository


class UserService:
    user_repository: UserRepository

    def __init__(
        self, user_repository: UserRepository = Depends()
    ) -> None:
        self.user_repository = user_repository

    def list(
        self, 
        page_size: Optional[int] = 100,
        start_index: Optional[int] = 0,
    ) -> List[Users]:
        return self.user_repository.list(
            page_size, start_index
        )
    
    def create(self, user: UserSchema) -> Users:
        return self.user_repository.create(
            Users(user=user.user, password=user.password, admin=user.admin)
        )
    
    def delete(self, id: int) -> None:
        return self.user_repository.delete(Users(id=id))
    
    def update(self, user: UserSchemaUpdate) -> Users:
        return self.user_repository.update(
            Users(password=user.password, id=user.id, user=user.user)
        )