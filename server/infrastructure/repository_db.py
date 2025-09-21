from server.domain.repository import VehicleRepository
from server.domain.models import Vehicle
from server.infrastructure.models_db import VehicleDB
from server.infrastructure.db import SessionLocal

class VehicleRepositoryDB(VehicleRepository):
    def search_by_filter(self, filters: dict):
        with SessionLocal() as session:
            query = session.query(VehicleDB)

            if "brand" in filters:
                query = query.filter(VehicleDB.brand.ilike(f"%{filters['brand']}%"))
            if "model" in filters:
                query = query.filter(VehicleDB.model.ilike(f"%{filters['model']}%"))
            if "fuel_type" in filters:
                query = query.filter(VehicleDB.fuel_type.ilike(f"%{filters['fuel_type']}%"))
            if "manufacture_year" in filters:
                query = query.filter(VehicleDB.manufacture_year >= filters['manufacture_year'])
            if "color" in filters:
                query = query.filter(VehicleDB.color.ilike(f"%{filters['color']}%"))
            if "mileage" in filters:
                query = query.filter(VehicleDB.mileage <= filters['mileage'])
            if "doors" in filters:
                query = query.filter(VehicleDB.doors == filters['doors'])
            if "transmission" in filters:
                query = query.filter(VehicleDB.transmission == filters['transmission'])
            if "ac" in filters:
                query = query.filter(VehicleDB.ac == filters['ac'])
            if "price" in filters:
                query = query.filter(VehicleDB.price <= filters['price'])

            results = query.all()

        return [Vehicle(
            id = vehicle.id,
            brand = vehicle.brand,
            model = vehicle.model,
            fuel_type=vehicle.fuel_type,
            manufacture_year= vehicle.manufacture_year,
            color = vehicle.color,
            mileage=vehicle.mileage,
            doors=vehicle.doors,
            transmission=vehicle.transmission,
            ac=vehicle.ac,
            price=vehicle.price
        ) for vehicle in results]



