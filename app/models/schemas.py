from typing import List, Optional
import ipaddress

from pydantic import BaseModel, validator, Field


class TaskModel(BaseModel):
    name: str
    priority: int
    status: str
    description: str
    created_at: str
    updated_at: str

    class Config:
        schema_extra = {
            "example": {
                "name": "read a book",
                "priority": 1,
                "status": "pending",
                "description": "read a book about python",
                "created_at": "2021-01-01 00:00:00",
                "updated_at": "2021-01-01 00:00:00",
            }
        }

    @validator("priority")
    def priority_must_be_integer(cls, v):
        if not isinstance(v, int):
            raise ValueError("Priority must be an integer")
        return v
