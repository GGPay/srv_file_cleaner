from .base import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class Product(Base):
    __tablename__ = "product"
    productID = Column(Integer, primary_key=True, nullable=False)
    partNumber = Column(String(255))
    factoryID = Column(Integer)


class Order(Base):
    __tablename__ = "order"
    orderID = Column(Integer, primary_key=True, nullable=False)


class OrderDetails(Base):
    __tablename__ = "orderDetails"
    orderDetailID = Column(Integer, primary_key=True, nullable=False)
    productID = Column(Integer, ForeignKey("product.productID"), nullable=False)
    description = Column(String(255))
