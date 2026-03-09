import time
import uuid
import logging

from fastapi import Request
from starlette.responses import Response

logger = logging.getLogger("app.request")


async def request_logging_middleware(request: Request, call_next):

    request_id = str(uuid.uuid4())

    request.state.request_id = request_id

    start_time = time.perf_counter()

    response: Response = await call_next(request)

    process_time = time.perf_counter() - start_time

    logger.info(
        "[%s] %s %s -> %s (%.4fs)",
        request_id,
        request.method,
        request.url.path,
        response.status_code,
        process_time,
    )

    response.headers["X-Request-ID"] = request_id

    return response
