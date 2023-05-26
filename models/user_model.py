from sqlalchemy import (
    Column,
    Integer,
    PrimaryKeyConstraint,
    String,
    Boolean
)
from models.base_model import EntityMeta


class Users(EntityMeta):
    __tablename__ = "users"
    id = Column(Integer, autoincrement=True)
    user = Column(String(40))
    password = Column(String(40))
    admin = Column(Boolean)
    PrimaryKeyConstraint(id)

    def normalize(self):
        return {
            "id": self.id.__str__(),
            "user": self.user.__str__(),
            "password": self.password.__str__(),
            "admin": self.admin.__str__(),
        }