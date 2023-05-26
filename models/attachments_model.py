from sqlalchemy import (
    Column,
    Integer,
    PrimaryKeyConstraint,
    String,
    ForeignKey
)
from models.base_model import EntityMeta


class Attachments(EntityMeta):
    __tablename__ = "attachments"
    id = Column(Integer, autoincrement=True)
    filename = Column(String(100))
    full_path = Column(String(100))
    id_aplication = Column(Integer, ForeignKey("aplication.id"))
    PrimaryKeyConstraint(id)

    def normalize(self):
        return {
            "id": self.id.__str__(),
            "filename": self.filename.__str__(),
            "full_path": self.full_path.__str__(),
            "id_aplication": self.id_aplication.__str__(),
        }