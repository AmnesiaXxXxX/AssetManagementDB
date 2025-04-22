from pydantic import BaseModel
from app.schemas.asset import AssetResponse


class CategoryBase(BaseModel):
    __tablename__ = "categories"

    id: int
    name: str
    description: str


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(BaseModel):
    id: int
    name: str
    description: str


class CategoryResponse(CategoryBase):
    id: int
    assets: list[AssetResponse]

    class Config:
        from_attributes = True
