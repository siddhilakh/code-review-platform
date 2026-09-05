from pydantic import BaseModel
from datetime import datetime


class RepositoryCreate(BaseModel):
    url: str


class RepositoryOut(BaseModel):
    id: int
    url: str
    created_at: datetime

    class Config:
        from_attributes = True  # lets Pydantic read straight from a SQLAlchemy object


class JobOut(BaseModel):
    id: str
    status: str
    progress: int
    repository_id: int
    created_at: datetime

    class Config:
        from_attributes = True