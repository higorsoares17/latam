from sqlalchemy import (
    Column,
    Integer,
    PrimaryKeyConstraint,
    String,
)
from sqlalchemy.orm import relationship

from models.base_model import EntityMeta


class Card(EntityMeta):
    __tablename__ = "cards"
    id = Column(Integer, autoincrement=True)
    name = Column(String(40), nullable=False)
    PrimaryKeyConstraint(id)
