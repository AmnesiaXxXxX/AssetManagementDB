from sqlalchemy import Column, Date, Float, ForeignKey, Integer
from sqlalchemy.orm import relationship

from app.db.database import Base


class Depreciation(Base):
    __tablename__ = "depreciations"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float, nullable=False)
    date = Column(Date, nullable=False)
    asset_id = Column(Integer, ForeignKey("assets.id"))

    asset = relationship("Asset", back_populates="depreciation_records")
