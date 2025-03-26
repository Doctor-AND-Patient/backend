from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import date
import enum

from schemas.base import BaseConfig
from schemas.doctors import Specialization


class RoleEnum(str, enum.Enum):
    admin = "admin"
    user = "user"
    doctor = "doctor"


class UserCreate(BaseModel):
    name: str
    birthday: date
    avatar: Optional[bytes] = None
    email: EmailStr
    phone: Optional[str] = None
    password: str
    role: RoleEnum
    organization_id: int
    specializations: List[Specialization] = []


class User(UserCreate, BaseConfig):
    id: int


class Role(BaseModel):
    id: int
    role: RoleEnum


class UserRole(BaseModel):
    user_id: int
    role_id: int
