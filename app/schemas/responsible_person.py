from pydantic import BaseModel
from app.schemas.asset import AssetResponse


class ResponsiblePersonBase(BaseModel):
    full_name: str
    personnel_number: str
    department_id: int


class ResponsiblePersonCreate(ResponsiblePersonBase):
    pass


class ResponsiblePersonUpdate(BaseModel):
    full_name: str | None = None
    personnel_number: str | None = None
    department_id: int | None = None


class ResponsiblePersonResponse(ResponsiblePersonBase):
    id: int
    assets: list[AssetResponse]

    class Config:
        from_attributes = True
