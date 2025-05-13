from sqlalchemy import Column, Integer, String, ForeignKey, Date, Float, Enum
from sqlalchemy.orm import relationship
import enum

from app.db.database import Base


class OperationType(enum.Enum):
    RECEIPT = "receipt"
    TRANSFER = "transfer"
    WRITE_OFF = "write_off"
    SALE = "sale"


class AssetMovement(Base):
    __tablename__ = "asset_movements"

    id = Column(Integer, primary_key=True, index=True)
    operation_date = Column(Date, nullable=False)
    operation_type = Column(Enum(OperationType), nullable=False)
    asset_id = Column(Integer, ForeignKey("assets.id"))
    amount = Column(Float, nullable=False)

    asset = relationship("Asset", back_populates="movements")
