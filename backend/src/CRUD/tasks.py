from sqlalchemy import insert, select

from backend.src.models.tasks import TasksORM
from backend.src.schemas.tasks import Task, TaskAdd


class TasksCRUD:
    def __init__(self, session):
        self.session = session

    async def create_task(self, data: TaskAdd) -> Task:
        add_stmt = insert(TasksORM).values(**data.model_dump()).returning(TasksORM)
        result = await self.session.execute(add_stmt)
        model = Task.model_validate(result.scalars().one(), from_attributes=True)
        return model
    
    async def get_tasks(self) -> list[Task]:
        query = select(TasksORM)
        result = await self.session.execute(query)
        models = [
            Task.model_validate(one, from_attributes=True) for one in result.scalars().all()
        ]
        return models
