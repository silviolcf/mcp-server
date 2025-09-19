from abc import ABC, abstractmethod
from typing import List, Dict
from .models import Vehicle

class VehicleRepository(ABC):
    @abstractmethod
    def search_by_filter(self, filters: Dict) -> List[Vehicle]:
        pass