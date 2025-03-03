from models.models.base import *
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

from models.models.users import User


class Request(Base):
    __tablename__ = 'requests'

    patient_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'), nullable=False)
    patient: Mapped[User] = relationship("User", foreign_keys=[patient_id], uselist=False)
    doctors: Mapped[list[User]] = relationship("User", secondary="request_doctors")
    complaint: Mapped[str] = mapped_column(String, nullable=False)
    analyzes: Mapped[str] = mapped_column(String, nullable=False)
    treatment: Mapped[str] = mapped_column(String, nullable=False)
    comment: Mapped[str] = mapped_column(String, nullable=False)


class SecondaryRequestDoctors(Base):
    __tablename__ = 'request_doctors'

    request_id: Mapped[int] = mapped_column(Integer, ForeignKey('requests.id'), primary_key=True)
    doctor_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'), primary_key=True)
