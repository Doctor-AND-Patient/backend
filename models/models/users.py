import enum

from sqlalchemy import String, Date, ForeignKey, Enum
from sqlalchemy.dialects.postgresql import BYTEA
from sqlalchemy.orm import relationship

from models.models.base import *
from models.models.doctors import Specialization


class Role(enum.Enum):
    admin = "admin"
    user = "user"
    doctor = "doctor"


class SecondaryRole(Base):
    __tablename__ = "roles"

    role: Mapped[Role] = mapped_column(Enum(Role), nullable=True)


class UserRole(Base):
    __tablename__ = 'user_roles'

    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'), primary_key=True)
    role_id: Mapped[int] = mapped_column(Integer, ForeignKey('roles.id'), primary_key=True)


class User(Base):
    __tablename__ = 'users'

    name: Mapped[str] = mapped_column(String(255), nullable=False)
    birthday: Mapped[Date] = mapped_column(Date, nullable=False)
    avatar: Mapped[bytes] = mapped_column(BYTEA, nullable=True)
    email: Mapped[str] = mapped_column(String(128), unique=True, nullable=False)
    phone: Mapped[str] = mapped_column(String(128), unique=True, nullable=True)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    organization_id: Mapped[int] = mapped_column(Integer, ForeignKey('organizations.id'), nullable=False)

    organization: Mapped["Organization"] = relationship("Organization", back_populates="workers")
    specializations: Mapped[list[Specialization]] = relationship("Specialization", secondary="doctor_specialization")
    roles: Mapped[list[SecondaryRole]] = relationship("SecondaryRole", secondary="user_roles")
