from sqlalchemy import insert, select, update, delete

from backend.src.models.tasks import TasksORM
from backend.src.schemas.tasks import Task, TaskAdd, TaskUpdate


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

    async def delete_task(self, task_id: int) -> None:
        delete_stmt = delete(TasksORM).where(TasksORM.id == task_id)
        await self.session.execute(delete_stmt)

    async def update_task(self, task_id: int, data: TaskUpdate) -> Task:
        update_stmt = (
            update(TasksORM)
            .where(TasksORM.id == task_id)
            .values(**data.model_dump(exclude_unset=True))
            .returning(TasksORM)
        )
        result = await self.session.execute(update_stmt)
        model = Task.model_validate(result.scalars().one(), from_attributes=True)
        return model
