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
    registration_date = Column(Date, nullable=False)
    cost = Column(Float, nullable=False)
    account_number = Column(String(20), nullable=False)

    responsible_person_id = Column(Integer, ForeignKey("responsible_persons.id"))
    category_id = Column(Integer, ForeignKey("categories.id"))
    department_id = Column(Integer, ForeignKey("departments.id"))

    responsible_person = relationship("ResponsiblePerson", back_populates="assets")
    category = relationship("Category", back_populates="assets")
    department = relationship("Department", back_populates="assets")
    depreciation_records = relationship("Depreciation", back_populates="asset")
    movements = relationship("AssetMovement", back_populates="asset")
