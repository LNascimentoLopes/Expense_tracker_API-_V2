from typing import Optional

from pydantic import BaseModel, EmailStr

class ExpenseCreate(BaseModel):
    description: Optional[str]
    value: Optional[float]
    class Config:
        from_attributes = True

class ExpenseUpdate(BaseModel):
    description:str
    value: float
    class Config:
        from_attributes = True

class TokenResponse(BaseModel):
    access_token: str
    token_type: str

class LoginRequest(BaseModel):
    email:EmailStr
    password: str

    class Config:
        from_attributes = True


class RegisterRequest(BaseModel):
    username:str
    email:EmailStr
    password:str

    class Config:
        from_attributes = True