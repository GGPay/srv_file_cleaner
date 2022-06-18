from .base import Base
from sqlalchemy import Column, Integer, String


class Product(Base):
    __tablename__ = "product"
    productID = Column(Integer, nullable=False)
    partNumber = Column(String(255))
