import pytest
from server.infrastructure.repository_db import VehicleRepositoryDB
from server.domain.models import Vehicle

def test_search_by_filter():
    """Testa busca por filtros no repositório"""
    repo = VehicleRepositoryDB()
    
    # Testa busca por marca
    results = repo.search_by_filter({"brand": "Toyota"})
    
    # Verifica que retorna uma lista
    assert isinstance(results, list)
    
    # Se houver resultados, verifica a estrutura
    if results:
        vehicle = results[0]
        assert hasattr(vehicle, 'brand')
        assert hasattr(vehicle, 'model')
        assert hasattr(vehicle, 'color')
        assert hasattr(vehicle, 'price')

def test_search_by_multiple_filters():
    """Testa busca com múltiplos filtros"""
    repo = VehicleRepositoryDB()
    
    # Testa busca com múltiplos filtros
    results = repo.search_by_filter({
        "brand": "Toyota",
        "color": "Red"
    })
    
    assert isinstance(results, list)
    
    # Se houver resultados, verifica se atendem aos filtros
    for vehicle in results:
        assert "Toyota" in vehicle.brand
        assert "Red" in vehicle.color
