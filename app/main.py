from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from app.routes.tasks import router as TaskRouterV1


app = FastAPI(
    title="Task API",
    description="API for Task management",
    version="1.0.0",
)


@app.get("/", response_class=RedirectResponse, include_in_schema=False)
async def docs():
    return RedirectResponse(url="/docs")


app.include_router(TaskRouterV1, tags=["Task"], prefix="/api/task")
