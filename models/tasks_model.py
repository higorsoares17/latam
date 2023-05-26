from sqlalchemy import (
    Column,
    Integer,
    PrimaryKeyConstraint,
    String,
    ForeignKey,
    DateTime
)
from models.base_model import EntityMeta


class Task(EntityMeta):
    __tablename__ = "task"
    id = Column(Integer, autoincrement=True)
    name = Column(String(100))
    due_date = Column(DateTime)
    assignee = Column(Integer, ForeignKey("users.id"))
    status = Column(String(100))
    section = Column(Integer, ForeignKey("task.id"))
    id_aplication = Column(Integer, ForeignKey("aplication.id"))
    PrimaryKeyConstraint(id)

    def normalize(self):
        return {
            "id": self.id.__str__(),
            "name": self.name.__str__(),
            "due_date": self.due_date.__str__(),
            "assignee": self.assignee.__str__(),
            "status": self.status.__str__(),
            "section": self.status.__str__(),
            "id_aplication": self.status.__str__(),
        }