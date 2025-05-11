from pydantic import BaseModel
from app.schemas.asset import AssetResponse


class DepartmentBase(BaseModel):
    code: str
    name: str


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
