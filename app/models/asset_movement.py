from app.db.database import Base
from sqlalchemy import (
    Column,
    Date,
    ForeignKey,
    Integer,
    String,
    UniqueConstraint,
)
from sqlalchemy.orm import relationship


class AssetMovement(Base):
    __tablename__ = "asset_movements"
    __table_args__ = (
        UniqueConstraint("inventory_number", name="uq_assets_inventory_number"),
    )
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    registration_date = Column(Date, nullable=False)
    responsible_person_id = Column(Integer, ForeignKey("responsible_persons.id"))
    category_id = Column(Integer, ForeignKey("categories.id"))
    department_id = Column(Integer, ForeignKey("departments.id"))
    operation_type_id = Column(
        Integer, ForeignKey("operation_type.operation_type_id")
    )
    operation_type = relationship(
        "OperationType",
        foreign_keys=[operation_type_id],  # Updated field name in relationship argument
    )
    responsible_person = relationship(
        "ResponsiblePerson", back_populates="asset_movements"
    )
    depreciation_records = relationship(
        "Depreciation", back_populates="asset_movements"
    )
    categories = relationship("Category", back_populates="asset_movements")
    department = relationship("Department", back_populates="asset_movements")
