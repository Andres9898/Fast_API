# schemas/provider.py
from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class ProviderBase(BaseModel):
    business_name: str
    legal_name: Optional[str]
    rfc: str
    email: EmailStr
    phone: Optional[str]
    address: Optional[str]
    city: Optional[str]
    state: Optional[str]
    postal_code: Optional[str]
    country: Optional[str]
    documents: Optional[str]
    status: Optional[str] = "pending"

class ProviderCreate(ProviderBase):
    pass

class ProviderOut(ProviderBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
