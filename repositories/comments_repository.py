from typing import List, Optional
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session, lazyload

from configs.Database import (
    get_db_connection,
)
from models.comments_model import Comments


class CommentsRepository:
    db: Session

    def __init__(self, db: Session = Depends(get_db_connection)) -> None:
        self.db = db

    def list(
        self,
        limit: Optional[int],
        start: Optional[int],
    ) -> List[Comments]:
        query = self.db.query(Comments)
        return query.offset(start).limit(limit).all()
    
    def create(self, comments:Comments) -> Comments:
        self.db.add(comments)
        self.db.commit()
        self.db.refresh(comments)
        return comments
    

    def delete(self, comments: Comments) -> None:
        del_comments = self.db.query(comments).filter_by(id=comments.id).first()
        if not del_comments:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id não encontrado")
        self.db.delete(del_comments)
        self.db.commit()
        self.db.flush()

    def update(self, comments: Comments) -> Comments:
        self.db.merge(comments)
        self.db.commit()
        return comments