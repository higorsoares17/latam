from models.comments_model import Comments
from fastapi import Depends
from typing import Optional, List
from schemas.comments_schema import CommentsSchema
from repositories.comments_repository import CommentsRepository


class CommentsService:
    comments_repository: CommentsRepository

    def __init__(
        self, comments_repository: CommentsRepository = Depends()
    ) -> None:
        self.comments_repository = comments_repository

    def list(
        self, 
        page_size: Optional[int] = 100,
        start_index: Optional[int] = 0,
    ) -> List[Comments]:
        return self.comments_repository.list(
            page_size, start_index
        )
    
    def create(self, comments: CommentsSchema) -> Comments:
        return self.comments_repository.create(
            Comments(
                id = comments.id,
                comentario = comments.comentario,
                id_user = comments.id_user,
                id_aplication = comments.id_aplication
            
            )
        )
    
    def delete(self, id: int) -> None:
        return self.comments_repository.delete(Comments(id=id))
    
    def update(self, comments: CommentsSchema) -> Comments:
        return self.comments_repository.update(
             Comments(
                id = comments.id,
                comentario = comments.comentario,
                id_user = comments.id_user,
                id_aplication = comments.id_aplication
            )
        )