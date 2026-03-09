from fastapi import Request
from app.core.responses import error_response
from typing import cast

from app.core.exceptions import (
    NotFoundException,
    ConflictException,
    BadRequestException,
)


async def not_found_handler(request: Request, exc: Exception):
    exc = cast(NotFoundException, exc)
    return error_response(exc.message, exc.error_type, 404)


async def conflict_handler(request: Request, exc: Exception):
    exc = cast(ConflictException, exc)
    return error_response(exc.message, exc.error_type, 409)


async def bad_request_handler(request: Request, exc: Exception):
    exc = cast(BadRequestException, exc)
    return error_response(exc.message, exc.error_type, 400)
