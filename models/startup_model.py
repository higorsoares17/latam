from sqlalchemy import (
    Column,
    Integer,
    PrimaryKeyConstraint,
    ForeignKey,
    String
)
from models.base_model import EntityMeta


class Startup(EntityMeta):
    __tablename__ = "startup"
    id = Column(Integer, autoincrement=True)
    name = Column(String(40))
    id_aplication = Column(Integer, ForeignKey("aplication.id"))
    PrimaryKeyConstraint(id)

    def normalize(self):
        return {
            "id": self.id.__str__(),
            "name": self.name.__str__(),
            "id_aplication": self.id_aplication.__str__(),
        }