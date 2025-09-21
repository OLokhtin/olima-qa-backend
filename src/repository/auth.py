import bcrypt
from fastapi import Request
from src.logger import logger
from src.security import security

def hash_password(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed.decode('utf-8')

def verify_password(password, hashed_password):
    return bcrypt.checkpw(password.encode(), hashed_password.encode('utf-8'))

async def get_uid_from_request(request: Request):
    try:
        token_name = security.config.JWT_ACCESS_COOKIE_NAME
        token = request.cookies.get(token_name)
        if not token:
            return None

        token_payload = security._decode_token(token)
        return token_payload.sub

    except Exception as e:
        logger.info(f"Could not get UID from token: {e}")
        return None