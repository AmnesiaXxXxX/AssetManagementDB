from sqlalchemy import (
    Column,
    Date,
    Float,
    ForeignKey,
    Integer,
    String,
    UniqueConstraint,
)
from sqlalchemy.orm import relationship

from app.db.database import Base


class Asset(Base):
    __tablename__ = "assets"
    __table_args__ = (
        UniqueConstraint("inventory_number", name="uq_assets_inventory_number"),
    )

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    inventory_number = Column(String(50), unique=True, index=True)
    cost: Column[float] = Column(Float, nullable=False)
    purchase_date = Column(Date, nullable=False)
    location = Column(String(100))
    status = Column(String(20), default="active")

    category_id = Column(Integer, ForeignKey("categories.id"))
    department_id = Column(Integer, ForeignKey("departments.id"))

    category = relationship("Category", back_populates="assets")
    department = relationship("Department", back_populates="assets")
    depreciation_records = relationship("Depreciation", back_populates="asset")
