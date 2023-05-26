from sqlalchemy import (
    Column,
    Integer,
    PrimaryKeyConstraint,
    String,
    ForeignKey
)
from models.base_model import EntityMeta


class Comments(EntityMeta):
    __tablename__ = "comments"
    id = Column(Integer, autoincrement=True)
    comentario = Column(String(100))
    id_user =  Column(Integer, ForeignKey("users.id"))
    id_aplication = Column(Integer, ForeignKey("aplication.id"))
    PrimaryKeyConstraint(id)

    def normalize(self):
        return {
            "id": self.id.__str__(),
            "comentario": self.comentario.__str__(),
            "id_user": self.id_user.__str__(),
            "id_aplication": self.id_aplication.__str__(),
        }