from domain.repository import VehicleRepository

class VehicleService:
    def __init__(self, repository: VehicleRepository):
        self.repository = repository
    
    def search_by_filter(self, filters: dict):
        return self.repository.search_by_filter(filters)