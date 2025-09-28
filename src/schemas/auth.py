from datetime import date

from pydantic import BaseModel, Field, EmailStr

class AuthScheme(BaseModel):
    user_email: EmailStr
    user_password: str = Field(min_length=8)

class UserScheme(AuthScheme):
    user_phone: str
    user_name: str
    user_surname: str
    user_birthday: date