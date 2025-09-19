from pydantic import BaseModel
from typing import Optional, Dict, Any

class VehicleFilterSchema(BaseModel):
    brand: Optional[str] = None
    model: Optional[str] = None
    color: Optional[str] = None
    fuel_type: Optional[str] = None
    manufacture_year: Optional[int] = None
    mileage: Optional[int] = None
    doors: Optional[int] = None
    transmission: Optional[str] = None
    ac: Optional[bool] = None
    price: Optional[float]  = None

class FilterWrapper(BaseModel):
    filters: Dict[str, Any]


