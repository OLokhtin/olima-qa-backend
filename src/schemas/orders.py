from datetime import date

from pydantic import BaseModel, Field, EmailStr

class OrderScheme(BaseModel):
    status: int = Field(ge=1)
    customer_full_name: str
    customer_phone: str
    customer_email: EmailStr
    delivery_address: str
    delivery_date: date
    total_amount: float = Field(gt=0)