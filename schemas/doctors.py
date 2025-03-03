from pydantic import BaseModel


class SpecializationBase(BaseModel):
    specialization_name: str


class Specialization(SpecializationBase):
    id: int


class SecondaryUserSpecialization(BaseModel):
    doctor_id: int
    specialization_id: int
