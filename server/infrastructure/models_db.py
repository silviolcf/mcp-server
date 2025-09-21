from sqlalchemy import Column, Integer, String, Float, Boolean
from server.infrastructure.db import Base

class VehicleDB(Base):
    __tablename__ = "vehicles"

    id = Column(Integer, primary_key=True, index=True)
    brand = Column(String, nullable=False)
    model = Column(String, nullable=False)
    manufacture_year = Column(Integer, nullable=False)
    fuel_type = Column(String, nullable=False)
    color = Column(String, nullable=False)
    mileage = Column(Integer, nullable=False)
    doors = Column(Integer, nullable=False)
    transmission = Column(String, nullable=False)
    ac = Column(Boolean, nullable=False)
    price = Column(Float, nullable=False)