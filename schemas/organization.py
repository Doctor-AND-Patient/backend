from typing import List
from pydantic import BaseModel
from schemas.base import BaseConfig
from schemas.user import User


class OrganizationBase(BaseModel):
    name: str
    address_id: int


class Organization(OrganizationBase, BaseConfig):
    id: int
    workers: List[User] = []


class AddressBase(BaseModel):
    city: str
    street: str
    zip: str


class Address(AddressBase, BaseConfig):
    id: int
    organizations: List[Organization] = []
