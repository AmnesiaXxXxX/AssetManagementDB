from sqlalchemy.orm import Session
from typing import List, Optional

from app.models.responsible_person import ResponsiblePerson
from app.schemas.responsible_person import ResponsiblePersonCreate, ResponsiblePersonUpdate


class ResponsiblePersonService:
    def get_all(self, db: Session) -> List[ResponsiblePerson]:
        return db.query(ResponsiblePerson).all()

    def get_by_id(self, db: Session, id: int) -> Optional[ResponsiblePerson]:
        return db.query(ResponsiblePerson).filter(ResponsiblePerson.id == id).first()

    def create(self, db: Session, person: ResponsiblePersonCreate) -> ResponsiblePerson:
        db_person = ResponsiblePerson(
            full_name=person.full_name,
            personnel_number=person.personnel_number,
            department_id=person.department_id
        )
        db.add(db_person)
        db.commit()
        db.refresh(db_person)
        return db_person

    def update(self, db: Session, id: int, person: ResponsiblePersonUpdate) -> Optional[ResponsiblePerson]:
        db_person = self.get_by_id(db, id)
        if not db_person:
            return None

        for key, value in person.model_dump(exclude_unset=True).items():
            setattr(db_person, key, value)

        db.commit()
        db.refresh(db_person)
        return db_person

    def delete(self, db: Session, id: int) -> bool:
        db_person = self.get_by_id(db, id)
        if not db_person:
            return False

        db.delete(db_person)
        db.commit()
        return True
