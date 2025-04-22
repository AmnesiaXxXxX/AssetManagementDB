from pydantic import BaseModel
from app.schemas.asset import AssetResponse


class DepartmentBase(BaseModel):
    __tablename__ = "categories"

    id: int
    name: str
    description: str


class DepartmentCreate(DepartmentBase):
    pass


class DepartmentUpdate(BaseModel):
    id: int
    name: str
    description: str


class DepartmentResponse(DepartmentBase):
    id: int
    assets: list[AssetResponse]
    
    class Config:
        from_attributes = True
