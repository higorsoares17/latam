from sqlalchemy import (
    Column,
    Integer,
    PrimaryKeyConstraint,
    ForeignKey,
    String,
)
from models.base_model import EntityMeta


class Card(EntityMeta):
    __tablename__ = "cards"
    id = Column(Integer, autoincrement=True)
    name = Column(String(40), nullable=True)
    id_column = Column(Integer, ForeignKey("columns.id"))
    PrimaryKeyConstraint(id)


    def normalize(self):
        return {
            "id": self.id.__str__(),
            "name": self.name.__str__(),
        }