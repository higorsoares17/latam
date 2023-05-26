from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TaskSchema(BaseModel):
    id: Optional[int]
    name: str
    due_date : datetime
    assignee : int 
    status : str
    section : int
    id_aplication : int

    class Config:
        orm_mode = True



