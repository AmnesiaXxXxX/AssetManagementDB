from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.department import (
    DepartmentCreate,
    DepartmentResponse,
    DepartmentUpdate,
)
from app.services.department_service import DepartmentService

router = APIRouter(tags=["departments"])


@router.post("/", response_model=DepartmentResponse)
def create_department(department: DepartmentCreate, db: Session = Depends(get_db)):
    try:
        return DepartmentService(db).create_department(department)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )


@router.get("/", response_model=List[DepartmentResponse])
def read_categories(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return DepartmentService(db).get_departments(skip=skip, limit=limit)


@router.get("/{department_id}", response_model=DepartmentResponse)
def read_department(department_id: int, db: Session = Depends(get_db)):
    department = DepartmentService(db).get_department(department_id)
    if department is None:
        raise HTTPException(status_code=404, detail="Department not found")
    return department


@router.put("/{department_id}", response_model=DepartmentResponse)
def update_department(
    department_id: int, department: DepartmentUpdate, db: Session = Depends(get_db)
):
    db_department = DepartmentService(db).update_department(department_id, department)
    if db_department is None:
        raise HTTPException(status_code=404, detail="Department not found")
    return db_department


@router.delete("/{department_id}", response_model=dict)
def delete_department(department_id: int, db: Session = Depends(get_db)):
    result = DepartmentService(db).delete_department(department_id)
    if not result:
        raise HTTPException(status_code=404, detail="Department not found")
    return {"message": "Department deleted successfully"}
