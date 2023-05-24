from sqlalchemy import (
    Column,
    Integer,
    PrimaryKeyConstraint,
    String,
)
from sqlalchemy.orm import relationship

from models.base_model import EntityMeta


class Columns(EntityMeta):
    __tablename__ = "columns"
    id = Column(Integer, autoincrement=True)
    name = Column(String(40), nullable=False)
    PrimaryKeyConstraint(id)

    def normalize(self):
        return {
            "id": self.id.__str__(),
            "name": self.name.__str__(),
        }