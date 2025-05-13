from sqlalchemy.orm import Session
from typing import List, Optional

from app.models.asset_movement import AssetMovement
from app.schemas.asset_movement import AssetMovementCreate, AssetMovementUpdate


class AssetMovementService:
    def get_all(self, db: Session) -> List[AssetMovement]:
        return db.query(AssetMovement).all()

    def get_by_id(self, db: Session, id: int) -> Optional[AssetMovement]:
        return db.query(AssetMovement).filter(AssetMovement.id == id).first()

    def create(self, db: Session, movement: AssetMovementCreate) -> AssetMovement:
        db_movement = AssetMovement(
            operation_date=movement.operation_date,
            operation_type=movement.operation_type,
            asset_id=movement.asset_id,
            amount=movement.amount,
        )
        db.add(db_movement)
        db.commit()
        db.refresh(db_movement)
        return db_movement

    def update(self, db: Session, id: int, movement: AssetMovementUpdate) -> Optional[AssetMovement]:
        db_movement = self.get_by_id(db, id)
        if not db_movement:
            return None

        for key, value in movement.model_dump(exclude_unset=True).items():
            setattr(db_movement, key, value)

        db.commit()
        db.refresh(db_movement)
        return db_movement

    def delete(self, db: Session, id: int) -> bool:
        db_movement = self.get_by_id(db, id)
        if not db_movement:
            return False

        db.delete(db_movement)
        db.commit()
        return True
