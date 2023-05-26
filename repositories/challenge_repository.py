from typing import List, Optional
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session, lazyload

from configs.Database import (
    get_db_connection,
)
from models.challenge_model import Challenge


class ChallengeRepository:
    db: Session

    def __init__(self, db: Session = Depends(get_db_connection)) -> None:
        self.db = db

    def list(
        self,
        limit: Optional[int],
        start: Optional[int],
    ) -> List[Challenge]:
        query = self.db.query(Challenge)
        return query.offset(start).limit(limit).all()
    
    def create(self, challenge:Challenge) -> Challenge:
        self.db.add(challenge)
        self.db.commit()
        self.db.refresh(challenge)
        return challenge
    

    def delete(self, challenge: Challenge) -> None:
        del_challenge = self.db.query(Challenge).filter_by(id=challenge.id).first()
        if not del_challenge:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id não encontrado")
        self.db.delete(del_challenge)
        self.db.commit()
        self.db.flush()

    def update(self, challenge: Challenge) -> Challenge:
        self.db.merge(challenge)
        self.db.commit()
        return challenge