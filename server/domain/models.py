from dataclasses import dataclass

@dataclass
class Vehicle:
    id: int
    brand: str
    model: str
    manufacture_year: int
    fuel_type: str
    color: str
    mileage: int
    doors: int
    transmission: str
    ac: bool
    price: float
    