from sqlalchemy import (
    Column,
    Integer,
    PrimaryKeyConstraint,
    String,
    ForeignKey
)
from models.base_model import EntityMeta


class Assignee(EntityMeta):
    __tablename__ = "assignee"
    id = Column(Integer, autoincrement=True)
    email = Column(String(40))
    name = Column(String(40))
    id_aplication = Column(Integer, ForeignKey("aplication.id"))
    id_user = Column(Integer, ForeignKey("user.id"))
    PrimaryKeyConstraint(id)

    def normalize(self):
        return {
            "id": self.id.__str__(),
            "email": self.email.__str__(),
            "name": self.name.__str__(),
            "id_aplication": self.id_aplication.__str__(),
            "id_user": self.id_user.__str__(),
        }