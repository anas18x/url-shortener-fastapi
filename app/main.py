from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.routes.urls import router as url_router
from app.db.connection import (
    open_pool,
    close_pool,
    check_database_connection,
)
from app.db.init_db import initialize_database


@asynccontextmanager
async def lifespan(app: FastAPI):
    open_pool()

    initialize_database()

    yield

    close_pool()


app = FastAPI(
    title="URL Shortener API",
    version="1.0.0",
    lifespan=lifespan,
)

app.include_router(url_router)


@app.get("/health")
def health_check():
    result = check_database_connection()

    return {
        "status": "ok",
        "database": result[0] == 1,
    }