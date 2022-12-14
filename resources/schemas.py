from enum import Enum
from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime, timedelta


class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None
    
class Role(str, Enum):
    admin = 'admin'
    user = 'user'

class UserBase(BaseModel):
    # username: str
    email: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None

class UserCreate(UserBase):
    password: str
    role: Role = Role.user

class UserUpdate(UserBase):
    password: str

class User(UserBase):
    id: int
    disabled: bool = False

    class Config:
        orm_mode = True
