from models.models.base import *
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

from models.models.users import User


class Organization(Base):
    __tablename__ = 'organizations'

    name: Mapped[str] = mapped_column(String(255), nullable=False)
    address_id: Mapped[int] = mapped_column(Integer, ForeignKey('addresses.id'), nullable=False)
    address: Mapped["Address"] = relationship("Address")
    workers: Mapped[list["User"]] = relationship("User", back_populates="organization")


class Address(Base):
    __tablename__ = 'addresses'

    city: Mapped[str] = mapped_column(String, nullable=False)
    street: Mapped[str] = mapped_column(String, nullable=False)
    zip: Mapped[str] = mapped_column(String, nullable=False)
