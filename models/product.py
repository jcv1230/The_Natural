from config.database import Base
from sqlalchemy import Column, Integer, Float, String

class Product(Base):
    __tablename__ = "Products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    description = Column(String(300), nullable=False)
    price = Column(Float, nullable=False)
    category = Column(String(15), nullable=False)
    

   