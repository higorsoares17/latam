from sqlalchemy import (
    Column,
    Integer,
    PrimaryKeyConstraint,
    ForeignKey,
    Float,
    DateTime
)
from models.base_model import EntityMeta


class Aplication(EntityMeta):
    __tablename__ = "aplication"
    id = Column(Integer, autoincrement=True)
    score = Column(Float)
    due_date = Column(DateTime)
    id_card =  Column(Integer, ForeignKey("cards.id"))
    PrimaryKeyConstraint(id)

    def normalize(self):
        return {
            "id": self.id.__str__(),
            "score": self.score.__str__(),
            "due_date": self.due_date.__str__(),
        }