from sqlalchemy import (
    Column, Integer, Enum as SQLAlchemyEnum
)
from enum import Enum
from app.db.database import Base


class OperationTypes(Enum):
    RECEIPT = "receipt"
    TRANSFER = "transfer"
    WRITE_OFF = "write_off"
    SALE = "sale"


class OperationType(Base):
    __tablename__ = "operation_type"
    id = Column(Integer, primary_key=True)
    operation_type = Column(SQLAlchemyEnum(OperationTypes), nullable=False)
    