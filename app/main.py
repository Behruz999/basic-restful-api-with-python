from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from contextlib import asynccontextmanager
from pathlib import Path

from app.core.logging import setup_logging
from app.api.v1.router import api_router
from app.core.config import settings
from app.core.exceptions import (
    NotFoundException,
    ConflictException,
    BadRequestException,
)
from app.core.exception_handlers import (
    not_found_handler,
    conflict_handler,
    bad_request_handler,
)
import logging
from app.core.middleware import request_logging_middleware

logger = logging.getLogger(__name__)

BASE_DIR = Path(__file__).resolve().parent


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Application starting...")
    yield
    logger.info("Application shutting down...")


def create_app() -> FastAPI:
    setup_logging()

    app = FastAPI(
        title=settings.PROJECT_NAME,
        lifespan=lifespan,
    )

    # Middleware
    app.middleware("http")(request_logging_middleware)

    # Root endpoint
    @app.get("/")
    async def root():
        return {
            "service": settings.PROJECT_NAME,
            "status": "running",
            "docs": "/docs",
        }

    # API routes
    app.include_router(api_router, prefix=settings.API_V1_PREFIX)

    # Static files
    app.mount(
        "/static",
        StaticFiles(directory=BASE_DIR / "static"),
        name="static",
    )

    # Exception handlers
    app.add_exception_handler(NotFoundException, not_found_handler)
    app.add_exception_handler(ConflictException, conflict_handler)
    app.add_exception_handler(BadRequestException, bad_request_handler)
    return app


app = create_app()
