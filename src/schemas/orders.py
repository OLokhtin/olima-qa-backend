from datetime import date

from pydantic import BaseModel, Field, EmailStr

class OrderScheme(BaseModel):
    status: int = Field(ge=1, le=6)
    customer_full_name: str
    customer_phone: str = Field(max_length=12)
    customer_email: EmailStr
    delivery_address: str
    delivery_date: date
    total_amount: int