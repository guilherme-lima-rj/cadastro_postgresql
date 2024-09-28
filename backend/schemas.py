from pydantic import BaseModel, PositiveFloat, EmailStr, Field, validator
from datetime import datetime
from typing import Optional

class CustomerBase(BaseModel):
    name: str
    surname: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    
    @validator('email', pre=True, always=True)
    def validate_email(cls, v):
        if v is None or v == '':
            return None
        return v
    
class CustomerCreate(CustomerBase):
    pass

class CustomerResponse(CustomerBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True #from_attributes

class CustomerUpdate(BaseModel):
    name: Optional[str]= None
    surname: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None