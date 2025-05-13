from sqlalchemy import Column, Date, Float, ForeignKey, Integer, Enum
from sqlalchemy.orm import relationship
import enum

from app.db.database import Base


class DepreciationMethod(enum.Enum):
    LINEAR = "linear"
    NONLINEAR = "nonlinear"
    PRODUCTION = "production"


class Depreciation(Base):
    __tablename__ = "depreciations"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float, nullable=False)
    period = Column(Date, nullable=False)
    depreciation_method = Column(Enum(DepreciationMethod), nullable=False)
    asset_id = Column(Integer, ForeignKey("asset_movements.id"))

    asset = relationship("asset_movements", back_populates="depreciation_records")
