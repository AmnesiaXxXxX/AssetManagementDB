from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.db.database import get_db
from app.schemas.depreciation import DepreciationCreate, DepreciationUpdate, DepreciationResponse
from app.services.depreciation_service import DepreciationService

router = APIRouter()
service = DepreciationService()

@router.get("", response_model=List[DepreciationResponse])
def get_all_depreciations(db: Session = Depends(get_db)):
    return service.get_all(db)

@router.get("/{id}", response_model=DepreciationResponse)
def get_depreciation(id: int, db: Session = Depends(get_db)):
    depreciation = service.get_by_id(db, id)
    if not depreciation:
        raise HTTPException(status_code=404, detail="Запись об амортизации не найдена")
    return depreciation

@router.post("", response_model=DepreciationResponse)
def create_depreciation(depreciation: DepreciationCreate, db: Session = Depends(get_db)):
    return service.create(db, depreciation)

@router.put("/{id}", response_model=DepreciationResponse)
def update_depreciation(id: int, depreciation: DepreciationUpdate, db: Session = Depends(get_db)):
    updated_depreciation = service.update(db, id, depreciation)
    if not updated_depreciation:
        raise HTTPException(status_code=404, detail="Запись об амортизации не найдена")
    return updated_depreciation

@router.delete("/{id}")
def delete_depreciation(id: int, db: Session = Depends(get_db)):
    if not service.delete(db, id):
        raise HTTPException(status_code=404, detail="Запись об амортизации не найдена")
    return {"message": "Запись об амортизации удалена"}
