from fastapi import APIRouter, Depends, status
from typing import List, Optional
from schemas.comments_schema import CommentsSchema
from services.comments_service import CommentsService


CommentsRouter = APIRouter(prefix="/v1/comments", tags=["Comments"])



@CommentsRouter.get("/", response_model=List[CommentsSchema])
def index(
    comments_service: CommentsService = Depends(),
    page_size: Optional[int] = 100,
    start_index: Optional[int] = 0,
):
    return [
        comments.normalize()
        for comments in comments_service.list(
            page_size, start_index
        )
    ]
    
@CommentsRouter.post(
    "/",
    response_model=CommentsSchema,
    status_code=status.HTTP_201_CREATED
)
def create(
    comments: CommentsSchema,
    comments_service: CommentsService = Depends(),
):
    return comments_service.create(comments)



@CommentsRouter.delete(
    "/{id}", status_code=status.HTTP_204_NO_CONTENT
)
def delete(id: int, comments_service: CommentsService = Depends()):
    return comments_service.delete(id)


@CommentsRouter.put(
    "/",
    response_model=CommentsSchema,
    status_code=status.HTTP_202_ACCEPTED
)
def update(
    comments: CommentsSchema,
    comments_service: CommentsSchema = Depends()
):
    return comments_service.update(comments)
