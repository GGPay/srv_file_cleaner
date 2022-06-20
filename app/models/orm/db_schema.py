from .base import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Product(Base):
    __tablename__ = "product"
    productID = Column(Integer, primary_key=True, nullable=False)
    partNumber = Column(String(255))
    factoryID = Column(Integer)
    # relationship
    pr_product = relationship("OrderDetails", backref="product")



class Order(Base):
    __tablename__ = "order"
    orderID = Column(Integer, primary_key=True, nullable=False)
    # relationship
    #or_product = relationship("OrderDetails", backref="odr_product")

    __mapper_args__ = {"eager_defaults": True}


class OrderDetails(Base):
    __tablename__ = "orderDetails"
    orderDetailID = Column(Integer, primary_key=True, nullable=False)
    productID = Column(Integer, ForeignKey("product.productID"), nullable=False)
    #orderID = Column(Integer, ForeignKey("order.orderID"), nullable=False)
    description = Column(String(255))
    # relationship
    #odr_product = relationship("Product", backref="pr_product", uselist=False)
    #odr_order = relationship("Order", backref="or_product", uselist=False)


