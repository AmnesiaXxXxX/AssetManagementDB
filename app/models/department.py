from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.database import Base


class Department(Base):
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(10), unique=True, nullable=False)
    name = Column(String(100), nullable=False)

    asset_movements = relationship("AssetMovement", back_populates="department")
    responsible_persons = relationship("ResponsiblePerson", back_populates="department")
