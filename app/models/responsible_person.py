from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.database import Base


class ResponsiblePerson(Base):
    __tablename__ = "responsible_persons"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(150), nullable=False)
    personnel_number = Column(String(50), unique=True, nullable=False)
    department_id = Column(Integer, ForeignKey("departments.id"))

    department = relationship("Department", back_populates="responsible_persons")
    assets = relationship("Asset", back_populates="responsible_person")
