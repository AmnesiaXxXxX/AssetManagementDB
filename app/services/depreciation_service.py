from sqlalchemy.orm import Session
from typing import List, Optional

from app.models.depreciation import Depreciation
from app.schemas.depreciation import DepreciationCreate, DepreciationUpdate


class DepreciationService:
    def get_all(self, db: Session) -> List[Depreciation]:
        return db.query(Depreciation).all()

    def get_by_id(self, db: Session, id: int) -> Optional[Depreciation]:
        return db.query(Depreciation).filter(Depreciation.id == id).first()

    def create(self, db: Session, depreciation: DepreciationCreate) -> Depreciation:
        db_depreciation = Depreciation(
            amount=depreciation.amount,
            period=depreciation.period,
            depreciation_method=depreciation.depreciation_method,
            asset_id=depreciation.asset_id
        )
        db.add(db_depreciation)
        db.commit()
        db.refresh(db_depreciation)
        return db_depreciation

    def update(self, db: Session, id: int, depreciation: DepreciationUpdate) -> Optional[Depreciation]:
        db_depreciation = self.get_by_id(db, id)
        if not db_depreciation:
            return None

        for key, value in depreciation.model_dump(exclude_unset=True).items():
            setattr(db_depreciation, key, value)

        db.commit()
        db.refresh(db_depreciation)
        return db_depreciation

    def delete(self, db: Session, id: int) -> bool:
        db_depreciation = self.get_by_id(db, id)
        if not db_depreciation:
            return False

        db.delete(db_depreciation)
        db.commit()
        return True
