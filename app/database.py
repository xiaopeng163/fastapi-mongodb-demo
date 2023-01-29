import os

import motor.motor_asyncio
from bson.objectid import ObjectId

from app.config import MONGO_URL, MONGO_DB_NAME


client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL)
database = client.get_database(MONGO_DB_NAME)
tasks_collection = database.get_collection("tasks_collection")


def bson_helper(bson_data) -> dict:
    bson_data["id"] = str(bson_data["_id"])
    bson_data.pop("_id")
    return bson_data


# Retrieve all tasks present in the database based on filter
async def retrieve_tasks(filter_dict={}):
    tasks = []
    async for task in tasks_collection.find(filter_dict):
        tasks.append(bson_helper(task))
    return tasks


# Add a new task into to the database
async def add_task(task_data: dict) -> dict:
    task = await tasks_collection.insert_one(task_data)
    new_task = await tasks_collection.find_one({"_id": task.inserted_id})
    return bson_helper(new_task)


# Retrieve a task with filter
async def retrieve_task(filter_dict) -> dict:
    if "id" in filter_dict:
        _id = ObjectId(filter_dict.pop("id"))
    task = await tasks_collection.find_one(filter_dict)
    if task:
        return bson_helper(task)


# Update a task with a matching ID
async def update_task(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    task = await tasks_collection.find_one({"_id": ObjectId(id)})
    if task:
        updated_task = await tasks_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_task:
            return True
        return False


# Delete a task from the database
async def delete_task(id: str):
    task = await tasks_collection.find_one({"_id": ObjectId(id)})
    if task:
        await tasks_collection.delete_one({"_id": ObjectId(id)})
        return True
