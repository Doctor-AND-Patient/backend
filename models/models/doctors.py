from sqlalchemy import ForeignKey, String

from models.models.base import *


class Specialization(Base):
    __tablename__ = 'specializations'

    specialization_name: Mapped[str] = mapped_column(String, nullable=True)


class SecondaryUserSpecialization(Base):
    __tablename__ = 'doctor_specialization'

    doctor_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'), primary_key=True)
    specialization_id: Mapped[str] = mapped_column(Integer, ForeignKey('specializations.id'), primary_key=True)
