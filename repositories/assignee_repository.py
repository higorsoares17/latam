from typing import List, Optional
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session, lazyload

from configs.Database import (
    get_db_connection,
)
from models.assignee_model import Assignee


class AssigneeRepository:
    db: Session

    def __init__(self, db: Session = Depends(get_db_connection)) -> None:
        self.db = db

    def list(
        self,
        limit: Optional[int],
        start: Optional[int],
    ) -> List[Assignee]:
        query = self.db.query(Assignee)
        return query.offset(start).limit(limit).all()
    
    def create(self, assignee:Assignee) -> Assignee:
        self.db.add(assignee)
        self.db.commit()
        self.db.refresh(assignee)
        return assignee
    

    def delete(self, assignee: Assignee) -> None:
        del_assigne = self.db.query(Assignee).filter_by(id=assignee.id).first()
        if not del_assigne:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id não encontrado")
        self.db.delete(del_assigne)
        self.db.commit()
        self.db.flush()

    def update(self, assignee: Assignee) -> Assignee:
        self.db.merge(assignee)
        self.db.commit()
        return assignee