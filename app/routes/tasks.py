from fastapi import APIRouter, Body, HTTPException
from fastapi.encoders import jsonable_encoder

from app.models.base import (
    ResponseModel,
)
from app.models.schemas import TaskModel


from app.database import (
    add_task,
    delete_task,
    retrieve_tasks,
    retrieve_task,
    update_task,
)


router = APIRouter()


@router.post("/", response_description="add task into database")
async def _add_task_data(task: TaskModel = Body(...)):
    task_dict = jsonable_encoder(task)
    if await retrieve_task(task_dict):
        raise HTTPException(
            status_code=400,
            detail=f"Task '{task.name}' already exists!",
        )
    new_task = await add_task(task_dict)
    return ResponseModel(new_task, "Task added successfully.")
