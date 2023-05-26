from sqlalchemy import (
    Column,
    Integer,
    PrimaryKeyConstraint,
    String,
    ForeignKey
)
from models.base_model import EntityMeta


class Challenge(EntityMeta):
    __tablename__ = "challenge"
    id = Column(Integer, autoincrement=True)
    desafio = Column(String(40))
    id_aplication = Column(Integer, ForeignKey("aplication.id"))
    PrimaryKeyConstraint(id)

    def normalize(self):
        return {
            "id": self.id.__str__(),
            "desafio": self.desafio.__str__(),
            "id_aplication": self.id_aplication.__str__(),
        }