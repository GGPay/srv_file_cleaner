from .base import Base
from sqlalchemy import Column, Integer, String


class Product(Base):
    __tablename__ = "product"
    productID = Column(Integer, primary_key=True, nullable=False)
    partNumber = Column(String(255))
    factoryID = Column(Integer)
