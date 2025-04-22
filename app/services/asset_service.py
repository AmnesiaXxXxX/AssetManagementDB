from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.asset import Asset
from app.schemas.asset import AssetCreate, AssetUpdate


class AssetService:
    def __init__(self, db: Session):
        self.db = db

    def _check_unique_inventory_number(
        self, inventory_number: str, exclude_id: int | None = None
    ):
        """Проверка уникальности инвентарного номера"""
        query = self.db.query(Asset).filter(Asset.inventory_number == inventory_number)
        if exclude_id:
            query = query.filter(Asset.id != exclude_id)
        if query.first():
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Инвентарный номер уже существует",
            )

    def create_asset(self, asset: AssetCreate) -> Asset:
        # Проверка уникальности перед созданием
        self._check_unique_inventory_number(asset.inventory_number)

        db_asset = Asset(**asset.model_dump())
        self.db.add(db_asset)
        self.db.commit()
        self.db.refresh(db_asset)
        return db_asset

    def get_asset(self, asset_id: int) -> Asset | None:
        return self.db.query(Asset).filter(Asset.id == asset_id).first()

    def get_assets(self, skip: int = 0, limit: int = 100) -> list[Asset]:
        return self.db.query(Asset).offset(skip).limit(limit).all()

    def update_asset(self, asset_id: int, asset: AssetUpdate) -> Asset | None:
        db_asset = self.get_asset(asset_id)
        if not db_asset:
            return None

        # Проверка уникальности при обновлении (если номер изменяется)
        if (
            asset.inventory_number
            and asset.inventory_number != db_asset.inventory_number
        ):
            self._check_unique_inventory_number(
                asset.inventory_number, exclude_id=asset_id
            )

        update_data = asset.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_asset, key, value)

        self.db.commit()
        self.db.refresh(db_asset)
        return db_asset

    def delete_asset(self, asset_id: int) -> bool:
        db_asset = self.get_asset(asset_id)
        if db_asset:
            self.db.delete(db_asset)
            self.db.commit()
            return True
        return False
