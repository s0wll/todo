import logging

from fastapi import APIRouter

from backend.src.services.tasks import TasksService
from backend.src.routers.dependencies import DBDep
from backend.src.schemas.tasks import TaskAdd, TaskUpdate


router = APIRouter(prefix="/api")


@router.get("/tasks")
async def get_tasks(db: DBDep):
    logging.info("Получение списка задач")
    tasks = await TasksService(db).get_tasks()
    logging.info("Успешное получение списка задач")
    return tasks


@router.post("/tasks")
async def add_task(db: DBDep, data: TaskAdd):
    logging.info("Добавление новой задачи")
    new_task = await TasksService(db).create_task(data=data)
    logging.info("Успешное добавление новой задачи")
    return {"status": "OK", "data": new_task}


@router.delete("/tasks/{task_id}")
async def delete_task(db: DBDep, task_id: int):
    logging.info("Удаление задачи")
    await TasksService(db).delete_task(task_id)
    logging.info("Успешное удаление задачи")
    return {"status": "OK"}


@router.patch("/tasks/{task_id}")
async def update_task(db: DBDep, task_id: int, data: TaskUpdate):
    logging.info("Обновление задачи")
    updated_task = await TasksService(db).update_task(task_id, data)
    logging.info("Успешное обновление задачи")
    return {"status": "OK", "data": updated_task}
