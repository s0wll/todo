from backend.src.utils.db_manager import DBManager
from backend.src.schemas.tasks import Task, TaskAdd, TaskUpdate


class TasksService:
    db: DBManager | None

    def __init__(self, db: DBManager | None = None) -> None:
        self.db = db

    async def create_task(self, data: TaskAdd) -> Task:
        new_task = await self.db.tasks.create_task(data=data)
        await self.db.commit()
        return new_task
    
    async def get_tasks(self) -> list[Task]:
        return await self.db.tasks.get_tasks()

    async def delete_task(self, task_id: int) -> None:
        await self.db.tasks.delete_task(task_id)
        await self.db.commit()

    async def update_task(self, task_id: int, data: TaskUpdate) -> Task:
        updated_task = await self.db.tasks.update_task(task_id, data)
        await self.db.commit()
        return updated_task