import sys
from pathlib import Path

from fastapi import FastAPI
import uvicorn

sys.path.append(str(Path(__file__).parent.parent.parent))

from backend.src.routers.tasks import router as router_tasks


app = FastAPI()


app.include_router(router_tasks)


if __name__ == "__main__":
    uvicorn.run("main:app", host="", reload=True)
