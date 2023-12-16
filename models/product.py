from config.database import Base
from sqlalchemy import Column, Integer, Float, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Product(Base):
    __tablename__ = "Products"
    id = Column(Integer, primary_key=True, index=True)
    supplier_id = Column(Integer, ForeignKey('Suppliers.supplier_id'))  # Esto es una clave foránea
    name = Column(String(50), nullable=False)
    description = Column(String(300), nullable=False)
    price = Column(Float, nullable=False)
    sub_category = Column(String, ForeignKey('Categories.sub_category'))  # Esto es una clave foránea
    #category = relationship("Category", back_populates="products")  # Esto es una relación muchos a uno
    #supplier = relationship("Supplier", back_populates="products")  # Esto es una relación muchos a uno
    
class Category(Base):
    __tablename__ = "Categories"
    categories = Column(String, nullable=False)
    sub_category = Column(String, nullable=False, primary_key=True)
    #products = relationship("Product", back_populates="sub_category")  # Esto es una relación uno a muchos
    
class Supplier(Base):
    __tablename__ = "Suppliers"
    supplier_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    address = Column(String(300), nullable=False)
    phone = Column(Integer, nullable=False)
    email = Column(String(50), nullable=False)
    city = Column(String(50), nullable=False)
    #products = relationship("Product", back_populates="Supplier_id")  # Esto es una relación uno a muchos


   