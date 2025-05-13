from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    Date,
    Float,
    UniqueConstraint,
)

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
    __table_args__ = (
        UniqueConstraint("inventory_number", name="uq_assets_inventory_number"),
    )
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    inventory_number = Column(String(50), unique=True, index=True)
    registration_date = Column(Date, nullable=False)
    cost = Column(Float, nullable=False)
    account_number = Column(String(20), nullable=False)

    responsible_person_id = Column(Integer, ForeignKey("responsible_persons.id"))
    category_id = Column(Integer, ForeignKey("categories.id"))
    department_id = Column(Integer, ForeignKey("departments.id"))

    responsible_person = relationship("ResponsiblePerson", back_populates="asset_movements")
    category = relationship("Category", back_populates="asset_movements")
    department = relationship("Department", back_populates="asset_movements")
    depreciation_records = relationship("Depreciation", back_populates="asset_movements")
