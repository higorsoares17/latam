from typing import List, Optional
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session, lazyload

from configs.Database import (
    get_db_connection,
)
from models.startup_model import Startup


class StartupRepository:
    db: Session

    def __init__(self, db: Session = Depends(get_db_connection)) -> None:
        self.db = db

    def list(
        self,
        limit: Optional[int],
        start: Optional[int],
    ) -> List[Startup]:
        query = self.db.query(Startup)
        return query.offset(start).limit(limit).all()
    
    def create(self, startup:Startup) -> Startup:
        self.db.add(startup)
        self.db.commit()
        self.db.refresh(startup)
        return startup
    

    def delete(self, startup: Startup) -> None:
        del_startup = self.db.query(Startup).filter_by(id=startup.id).first()
        if not del_startup:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id não encontrado")
        self.db.delete(del_startup)
        self.db.commit()
        self.db.flush()

    def update(self, startup: Startup) -> Startup:
        self.db.merge(startup)
        self.db.commit()
        return startup