from sqlalchemy.orm import Session

from app.models.department import Department
from app.schemas.department import DepartmentCreate, DepartmentUpdate


class DepartmentService:
    def __init__(self, db: Session):
        self.db = db

    def create_department(self, department: DepartmentCreate) -> Department:
        db_department = Department(**department.model_dump())
        self.db.add(db_department)
        self.db.commit()
        self.db.refresh(db_department)
        return db_department

    def get_department(self, department_id: int) -> Department | None:
        return self.db.query(Department).filter(Department.id == department_id).first()

    def get_departments(self, skip: int = 0, limit: int = 100) -> list[Department]:
        return self.db.query(Department).offset(skip).limit(limit).all()

    def update_department(
        self, department_id: int, department: DepartmentUpdate
    ) -> Department | None:
        db_department = self.get_department(department_id)
        if not db_department:
            return None

        update_data = department.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_department, key, value)

        self.db.commit()
        self.db.refresh(db_department)
        return db_department

    def delete_department(self, department_id: int) -> bool:
        db_department = self.get_department(department_id)
        if db_department:
            self.db.delete(db_department)
            self.db.commit()
            return True
        return False
