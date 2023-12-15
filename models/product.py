from config.database import Base
from sqlalchemy import Column, Integer, Float, String

class Product(Base):
    __tablename__ = "Products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    description = Column(String(300), nullable=False)
    price = Column(Float, nullable=False)
    sub_category = Column(String, primary_key=True, nullable=False)
    
class Category(Base):
    __tablename__ = "Categories"
    categories = Column(String(50), nullable=False)
    sub_category = Column(String, nullable=False, primary_key=True)
    


   