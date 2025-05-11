from datetime import date
from pydantic import BaseModel
from app.models.depreciation import DepreciationMethod


class DepreciationBase(BaseModel):
    amount: float
    period: date
    depreciation_method: DepreciationMethod
    asset_id: int


class DepreciationCreate(DepreciationBase):
    pass


class DepreciationUpdate(BaseModel):
    amount: float | None = None
    period: date | None = None
    depreciation_method: DepreciationMethod | None = None


class DepreciationResponse(DepreciationBase):
    id: int

    class Config:
        from_attributes = True
