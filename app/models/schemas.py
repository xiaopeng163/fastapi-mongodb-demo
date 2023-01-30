from typing import List, Optional
import ipaddress

from pydantic import BaseModel, validator, Field


class TaskModel(BaseModel):
    name: str
    priority: int
    status: str

    class Config:
        schema_extra = {
            "example": {"name": "read a book", "priority": 1, "status": "pending"}
        }

    @validator("priority")
    def priority_must_be_integer(cls, v):
        if not isinstance(v, int):
            raise ValueError("Priority must be an integer")
        return v


class TaskUpdateModel(BaseModel):

    priority: int

    class Config:
        schema_extra = {"example": {"priority": 1}}

    @validator("priority")
    def priority_must_be_integer(cls, v):
        if not isinstance(v, int):
            raise ValueError("Priority must be an integer")
        return v
