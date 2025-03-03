from typing import List
from pydantic import BaseModel
from schemas.base import BaseConfig
from schemas.user import User


class RequestBase(BaseModel):
    patient_id: int
    complaint: str
    analyzes: str
    treatment: str
    comment: str


class Request(RequestBase, BaseConfig):
    id: int
    patient: User
    doctors: List[User] = []


class SecondaryRequestDoctors(BaseModel):
    request_id: int
    doctor_id: int
