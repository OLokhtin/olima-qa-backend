from authx import AuthX, AuthXConfig
from dotenv import load_dotenv
import os
from datetime import timedelta

config = AuthXConfig()
load_dotenv()
config.JWT_ALGORITHM = "HS256"
config.JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
config.JWT_ACCESS_COOKIE_NAME = "X-Access-Token"
config.JWT_TOKEN_LOCATION = ["cookies"]
config.JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=60)
config.JWT_COOKIE_SECURE = False # HTTP - False, HTTPS - True
config.JWT_COOKIE_SAMESITE = "lax"
config.JWT_COOKIE_CSRF_PROTECT = False

security = AuthX(config=config)