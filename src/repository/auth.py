from authx import RequestToken
import bcrypt

from src.security import security

def get_current_user(token: RequestToken = security.get_token_from_request):
    return token

def hash_password(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed.decode('utf-8')

def verify_password(password, hashed_password):
    return bcrypt.checkpw(password.encode(), hashed_password.encode('utf-8'))