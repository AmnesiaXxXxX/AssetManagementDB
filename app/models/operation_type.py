from enum import Enum

from app.db.database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy import Enum as SQLAlchemyEnum


class OperationTypes(Enum):
    RECEIPT = "receipt"
    TRANSFER = "transfer"
    WRITE_OFF = "write_off"
    SALE = "sale"


class OperationType(Base):
    __tablename__ = "operation_type"
    id = Column(Integer, primary_key=True, autoincrement=True)
    operation_type = Column(String, SQLAlchemyEnum(OperationTypes), nullable=False)
