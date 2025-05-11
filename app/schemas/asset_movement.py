from datetime import date
from pydantic import BaseModel
from app.models.asset_movement import OperationType


class AssetMovementBase(BaseModel):
    operation_date: date
    operation_type: OperationType
    asset_id: int
    amount: float
    document_base: str | None = None


class AssetMovementCreate(AssetMovementBase):
    pass


class AssetMovementUpdate(BaseModel):
    operation_date: date | None = None
    operation_type: OperationType | None = None
    amount: float | None = None
    document_base: str | None = None


class AssetMovementResponse(AssetMovementBase):
    id: int

    class Config:
        from_attributes = True
