from typing import List, Union

from fastapi import APIRouter, Body, HTTPException, status
from fastapi.encoders import jsonable_encoder

from app.models.base import (
    ResponseModel,
)
from app.models.schemas import TaskModel, TaskUpdateModel


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


@router.get("/", response_description="get tasks from database")
async def _get_task_data(name: Union[str, None] = None):
    if name:
        tasks = await retrieve_tasks(filter_dict={"name": name})
    else:
        tasks = await retrieve_tasks()
    return ResponseModel(tasks, "Tasks data retrieved successfully")


@router.put("/{id}", response_description="update task's priority")
async def _update_label_data(id: str, req: TaskUpdateModel):
    req = jsonable_encoder(req)
    updated_task = await update_task(id, req)
    if updated_task:
        return ResponseModel(
            f"Task with ID: {id} update is successful",
            "Task priority updated successfully",
        )
    return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="failed")


@router.delete("/{id}", response_description="delete task from database")
async def _delete_task_data(id: str):
    deleted_task = await delete_task(id)
    if deleted_task:
        return ResponseModel(f"Task with ID: {id} removed", "Task deleted successfully")
    return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="failed")
