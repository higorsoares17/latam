from models.assignee_model import Assignee
from fastapi import Depends
from typing import Optional, List
from schemas.assignee_schema import AssigneeSchema
from repositories.assignee_repository import AssigneeRepository


class AssigneeService:
    assignee_respository: AssigneeRepository

    def __init__(
        self, assignee_respository: AssigneeRepository = Depends()
    ) -> None:
        self.assignee_respository = assignee_respository

    def list(
        self, 
        page_size: Optional[int] = 100,
        start_index: Optional[int] = 0,
    ) -> List[Assignee]:
        return self.assignee_respository.list(
            page_size, start_index
        )
    
    def create(self, assignee: AssigneeSchema) -> Assignee:
        return self.assignee_respository.create(
            Assignee(
                id=assignee.id,
                email=assignee.email,
                name = assignee.name,
                id_aplication = assignee.id_aplication,
                id_user = assignee.id_user
            )
        )
    
    def delete(self, id: int) -> None:
        return self.assignee_respository.delete(Assignee(id=id))
    
    def update(self, assignee: AssigneeSchema) -> Assignee:
        return self.assignee_respository.update(
            Assignee(
                id=assignee.id,
                email=assignee.email,
                name = assignee.name,
                id_aplication = assignee.id_aplication,
                id_user = assignee.id_user
            )
        )