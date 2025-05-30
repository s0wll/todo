from backend.src.utils.db_manager import DBManager
from backend.src.schemas.tasks import Task, TaskAdd


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
