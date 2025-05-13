from datetime import date
from pydantic import BaseModel


class AssetMovementBase(BaseModel):
    name: str
    inventory_number: str
    registration_date: date
    cost: float
    account_number: str
    responsible_person_id: int
    category_id: int
    department_id: int


class AssetMovementCreate(AssetMovementBase):
    pass


class AssetMovementUpdate(BaseModel):
    name: str | None = None
    inventory_number: str | None = None
    registration_date: date | None = None
    cost: float | None = None
    account_number: str | None = None
    responsible_person_id: int | None = None
    category_id: int | None = None
    department_id: int | None = None


class AssetMovementResponse(AssetMovementBase):
    id: int

    class Config:
        from_attributes = True
