from typing import List, Optional
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from configs.Database import (
    get_db_connection,
)
from models.user_model import Users


class UserRepository:
    db: Session

    def __init__(self, db: Session = Depends(get_db_connection)) -> None:
        self.db = db

    def list(
        self,
        limit: Optional[int],
        start: Optional[int],
    ) -> List[Users]:
        query = self.db.query(Users)
        return query.offset(start).limit(limit).all()
    

    def create(self, user:Users) -> Users:
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
    

    def delete(self, user: Users) -> None:
        del_user = self.db.query(Users).filter_by(id=user.id).first()
        if not del_user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id não encontrado")
        self.db.delete(del_user)
        self.db.commit()
        self.db.flush()

    def update(self, user: Users) -> Users:
        self.db.merge(user)
        self.db.commit()
        return user