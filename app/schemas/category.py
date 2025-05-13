from pydantic import BaseModel
from app.schemas.asset_movement import AssetMovementResponse


class CategoryBase(BaseModel):
    code: str
    name: str


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(BaseModel):
    id: int
    name: str
    description: str


class CategoryResponse(CategoryBase):
    id: int
    assets: list[AssetMovementResponse]

    class Config:
        from_attributes = True
