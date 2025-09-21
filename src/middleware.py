from fastapi import Request
from src.logger import logger
from src.repository.auth import get_uid_from_request

async def log_middleware(request: Request, call_next):
    method = request.method
    url = request.url.path
    uid = await get_uid_from_request(request)

    log_message = f"Request: {method} {url}"
    if uid:
        log_message += f" from user_id={uid}"
    logger.info(log_message)

    response = await call_next(request)
    status_code = response.status_code

    response_log = f"Response: {method} {url} returned {status_code}"
    if uid:
        response_log += f" to user_id={uid}"

    logger.info(response_log)
    return response