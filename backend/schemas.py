from pydantic import BaseModel, PositiveFloat, EmailStr, validator, Field
from datetime import datetime
from typing import Optional

class CustomerBase(BaseModel):
    name: str
    surname: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    
class CustomerCreate(CustomerBase):
    pass

class CustomerResponse(CustomerBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True #from_attributes

class CustomerUpdate(BaseModel):
    name: Optional[str]= None
    surname: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None