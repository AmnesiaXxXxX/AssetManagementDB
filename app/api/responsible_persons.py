from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.db.database import get_db
from app.schemas.responsible_person import (
    ResponsiblePersonCreate,
    ResponsiblePersonUpdate,
    ResponsiblePersonResponse,
)
from app.services.responsible_person_service import ResponsiblePersonService

router = APIRouter(tags=["responsible_persons"])
service = ResponsiblePersonService()


@router.get("", response_model=List[ResponsiblePersonResponse])
def get_all_responsible_persons(db: Session = Depends(get_db)):
    return service.get_all(db)


@router.get("/{id}", response_model=ResponsiblePersonResponse)
def get_responsible_person(id: int, db: Session = Depends(get_db)):
    person = service.get_by_id(db, id)
    if not person:
        raise HTTPException(
            status_code=404, detail="Материально-ответственное лицо не найдено"
        )
    return person


@router.post("", response_model=ResponsiblePersonResponse)
def create_responsible_person(
    person: ResponsiblePersonCreate, db: Session = Depends(get_db)
):
    return service.create(db, person)


@router.put("/{id}", response_model=ResponsiblePersonResponse)
def update_responsible_person(
    id: int, person: ResponsiblePersonUpdate, db: Session = Depends(get_db)
):
    updated_person = service.update(db, id, person)
    if not updated_person:
        raise HTTPException(
            status_code=404, detail="Материально-ответственное лицо не найдено"
        )
    return updated_person


@router.delete("/{id}")
def delete_responsible_person(id: int, db: Session = Depends(get_db)):
    if not service.delete(db, id):
        raise HTTPException(
            status_code=404, detail="Материально-ответственное лицо не найдено"
        )
    return {"message": "Материально-ответственное лицо удалено"}
