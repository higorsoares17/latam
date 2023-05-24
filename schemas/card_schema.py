from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class StartupSchema(BaseModel):
    id: int
    name: str


class ChallengeSchema(BaseModel):
    id: int
    name: str


class AssigneeSchema(BaseModel):
    id: int
    email: str
    name: str


class CommentsSchema(BaseModel):
    id: int
    author = AssigneeSchema


class AttachmentsSchema(BaseModel):
    id: int
    filename: str
    full_path: str


class SectionSchema(BaseModel):
    id: int
    name: str


class TasksSchema(BaseModel):
    id: int
    name: str
    due_date = datetime
    assignee = AssigneeSchema
    status = str
    section = SectionSchema


class AplicationSchema(BaseModel):
    id: int
    startup: Optional[StartupSchema]
    challenge: Optional[ChallengeSchema]
    score: float
    assignee: Optional[AssigneeSchema]
    comments: Optional[CommentsSchema]
    due_date: datetime
    attachments: Optional[AttachmentsSchema]
    tasks: Optional[TasksSchema]

class CardSchema(BaseModel):
    id: Optional[int]
    name: str

    class Config:
        orm_mode = True


class CardSchemaCreate(BaseModel):
    name: str
    id_column : int

    class Config:
        orm_mode = True


class CardSchemaUpdate(BaseModel):
    id: Optional[int]
    name: str
    id_column : int
