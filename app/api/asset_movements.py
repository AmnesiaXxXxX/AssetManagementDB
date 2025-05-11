from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.db.database import get_db
from app.schemas.asset_movement import AssetMovementCreate, AssetMovementUpdate, AssetMovementResponse
from app.services.asset_movement_service import AssetMovementService

router = APIRouter()
service = AssetMovementService()

@router.get("", response_model=List[AssetMovementResponse])
def get_all_movements(db: Session = Depends(get_db)):
    return service.get_all(db)

@router.get("/{id}", response_model=AssetMovementResponse)
def get_movement(id: int, db: Session = Depends(get_db)):
    movement = service.get_by_id(db, id)
    if not movement:
        raise HTTPException(status_code=404, detail="Движение ОС не найдено")
    return movement

@router.post("", response_model=AssetMovementResponse)
def create_movement(movement: AssetMovementCreate, db: Session = Depends(get_db)):
    return service.create(db, movement)

@router.put("/{id}", response_model=AssetMovementResponse)
def update_movement(id: int, movement: AssetMovementUpdate, db: Session = Depends(get_db)):
    updated_movement = service.update(db, id, movement)
    if not updated_movement:
        raise HTTPException(status_code=404, detail="Движение ОС не найдено")
    return updated_movement

@router.delete("/{id}")
def delete_movement(id: int, db: Session = Depends(get_db)):
    if not service.delete(db, id):
        raise HTTPException(status_code=404, detail="Движение ОС не найдено")
    return {"message": "Движение ОС удалено"}
