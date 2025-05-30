from fastapi import APIRouter

from backend.src.services.tasks import TasksService
from backend.src.routers.dependencies import DBDep
from backend.src.schemas.tasks import TaskAdd


router = APIRouter(prefix="/api")


@router.get("/tasks")
async def get_tasks(db: DBDep):
    tasks = await TasksService(db).get_tasks()
    return tasks


@router.post("/tasks")
async def add_task(db: DBDep, data: TaskAdd):
    new_task = await TasksService(db).create_task(data=data)
    return {"status": "OK", "data": new_task}