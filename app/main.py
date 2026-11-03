from fastapi import FastAPI

from app.api.routes import router
from app.config import settings

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="Oracle-connected AI chat assistant backend",
)


@app.get("/health")
def healthcheck():
    return {"status": "ok"}


app.include_router(router, prefix="/api/v1")
