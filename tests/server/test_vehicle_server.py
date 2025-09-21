import pytest
from application.services import VehicleService
from infrastructure.repository_db import VehicleRepositoryDB

@pytest.mark.asyncio
async def test_search_by_filter_returns_expected_data(monkeypatch):
    # Mock do repositório para não bater no banco
    class FakeRepo:
        async def search_by_filter(self, filters):
            return [
                type("Vehicle", (), {"id": 1, "brand": "Fiat", "model": "Argo",
                                     "fuel_type": "Gasolina", "manufacture_year": 2022,
                                     "color": "Azul", "mileage": 10000,
                                     "doors": 4, "transmission": "Automático",
                                     "ac": True, "price": 50000})
            ]

    service = VehicleService(FakeRepo())
    results = await service.search_by_filter({"color": "azul"})

    assert len(results) == 1
    assert results[0].brand == "Fiat"
    assert results[0].color == "Azul"
