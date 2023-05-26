from fastapi import APIRouter, Depends, status
from typing import List, Optional
from schemas.user_schema import UserSchema, UserSchemaUpdate
from services.user_service import UserService


UserRouter = APIRouter(prefix="/v1/user", tags=["Users"])



@UserRouter.get("/", response_model=List[UserSchema])
def index(
    user_service: UserService = Depends(),
    page_size: Optional[int] = 100,
    start_index: Optional[int] = 0,
):
    return [
        user.normalize()
        for user in user_service.list(
            page_size, start_index
        )
    ]
    
@UserRouter.post(
    "/",
    response_model=UserSchema,
    status_code=status.HTTP_201_CREATED
)
def create(
    user: UserSchema,
    user_service: UserService = Depends(),
):
    return user_service.create(user)



@UserRouter.delete(
    "/{id}", status_code=status.HTTP_204_NO_CONTENT
)
def delete(id: int, user_service: UserService = Depends()):
    return user_service.delete(id)


@UserRouter.put(
    "/",
    response_model=UserSchema,
    status_code=status.HTTP_202_ACCEPTED
)
def update(
    user: UserSchemaUpdate,
    user_service: UserService = Depends()
):
    return user_service.update(user)
