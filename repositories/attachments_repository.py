from typing import List, Optional
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session, lazyload

from configs.Database import (
    get_db_connection,
)
from models.attachments_model import Attachments


class AttachmentsRepository:
    db: Session

    def __init__(self, db: Session = Depends(get_db_connection)) -> None:
        self.db = db

    def list(
        self,
        limit: Optional[int],
        start: Optional[int],
    ) -> List[Attachments]:
        query = self.db.query(Attachments)
        return query.offset(start).limit(limit).all()
    
    def create(self, attachments:Attachments) -> Attachments:
        self.db.add(attachments)
        self.db.commit()
        self.db.refresh(attachments)
        return attachments
    

    def delete(self, attachments: Attachments) -> None:
        del_attachments = self.db.query(Attachments).filter_by(id=attachments.id).first()
        if not del_attachments:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id não encontrado")
        self.db.delete(del_attachments)
        self.db.commit()
        self.db.flush()

    def update(self, attachments: Attachments) -> Attachments:
        self.db.merge(attachments)
        self.db.commit()
        return attachments