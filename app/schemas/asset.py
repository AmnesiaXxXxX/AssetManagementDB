from datetime import date

from pydantic import BaseModel, field_validator


class AssetBase(BaseModel):
    name: str
    inventory_number: str
    cost: float
    registration_date: date
    account_number: str
    responsible_person_id: int
    category_id: int
    department_id: int

    @field_validator("inventory_number")
    def validate_inventory_number(cls, v: str):
        if len(v) < 3:
            raise ValueError("Инвентарный номер должен содержать минимум 3 символа")
        return v.upper()


class AssetCreate(AssetBase):
    pass


class AssetUpdate(BaseModel):
    name: str | None = None
    inventory_number: str | None = None
    cost: float | None = None
    location: str | None = None
    status: str | None = None
    category_id: int | None = None
    department_id: int | None = None


class AssetResponse(AssetBase):
    id: int

    class Config:
        from_attributes = True
