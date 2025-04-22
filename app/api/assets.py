from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.asset import AssetCreate, AssetResponse, AssetUpdate
from app.services.asset_service import AssetService

router = APIRouter(tags=["assets"])


@router.post("/", response_model=AssetResponse)
def create_asset(asset: AssetCreate, db: Session = Depends(get_db)):
    try:
        return AssetService(db).create_asset(asset)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )


@router.get("/", response_model=List[AssetResponse])
def read_assets(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return AssetService(db).get_assets(skip=skip, limit=limit)


@router.get("/{asset_id}", response_model=AssetResponse)
def read_asset(asset_id: int, db: Session = Depends(get_db)):
    asset = AssetService(db).get_asset(asset_id)
    if asset is None:
        raise HTTPException(status_code=404, detail="Asset not found")
    return asset


@router.put("/{asset_id}", response_model=AssetResponse)
def update_asset(asset_id: int, asset: AssetUpdate, db: Session = Depends(get_db)):
    db_asset = AssetService(db).update_asset(asset_id, asset)
    if db_asset is None:
        raise HTTPException(status_code=404, detail="Asset not found")
    return db_asset


@router.delete("/{asset_id}", response_model=dict)
def delete_asset(asset_id: int, db: Session = Depends(get_db)):
    result = AssetService(db).delete_asset(asset_id)
    if not result:
        raise HTTPException(status_code=404, detail="Asset not found")
    return {"message": "Asset deleted successfully"}
