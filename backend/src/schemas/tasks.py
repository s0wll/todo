from pydantic import BaseModel, Field


class TaskAdd(BaseModel):
    title: str = Field(max_length=200)
    completed: bool = False


class Task(TaskAdd):
    id: int


class TaskUpdate(BaseModel):
    completed: bool = Field(description="Статус выполнения задачи")
