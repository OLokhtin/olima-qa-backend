from fastapi import Request
from src.logger import logger

async def log_middleware(request: Request, call_next):
    client_ip = request.client.host
    method = request.method
    url = request.url.path
    logger.info(f"Request: {method} {url} from {client_ip}")

    response = await call_next (request)
    status_code = response.status_code
    logger.info(f"Response: {method} {url} returned {status_code} to {client_ip}")
    return response