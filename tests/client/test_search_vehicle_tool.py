import pytest
from client.infrastructure.tools.search_vehicle_tool import SearchVehicleTool
from client.domain.schemas import VehicleFilterSchema

class TestSearchVehicleTool:
    
    def test_tool_initialization(self):
        """Testa inicialização da ferramenta"""
        tool = SearchVehicleTool()
        
        assert tool.name == "search_vehicle"
        assert "Busca veículos" in tool.description
        assert tool.args_schema == VehicleFilterSchema
    
    def test_tool_description_contains_filters(self):
        """Testa se a descrição contém informações sobre filtros"""
        tool = SearchVehicleTool()
        
        description = tool.description.lower()
        assert "brand" in description
        assert "model" in description
        assert "color" in description
        assert "price" in description
        assert "transmission" in description
    
    @pytest.mark.asyncio
    async def test_arun_with_valid_filters(self, monkeypatch):
        """Testa execução com filtros válidos"""
        tool = SearchVehicleTool()
        
        # Mock do MCPClient
        class MockMCPClient:
            async def search_vehicle(self, filters):
                return [
                    {
                        "id": 1, "brand": "Toyota", "model": "Corolla",
                        "fuel_type": "Gasolina", "manufacture_year": 2022,
                        "color": "Azul", "mileage": 50000,
                        "doors": 4, "transmission": "AT", "ac": True, "price": 75000.0
                    }
                ]
        
        monkeypatch.setattr("client.infrastructure.tools.search_vehicle_tool.MCPClient", MockMCPClient)
        
        result = await tool._arun(brand="Toyota", color="Azul")
        
        assert len(result) == 1
        assert result[0]["brand"] == "Toyota"
        assert result[0]["color"] == "Azul"
    
    @pytest.mark.asyncio
    async def test_arun_filters_none_values(self, monkeypatch):
        """Testa que valores None são filtrados"""
        tool = SearchVehicleTool()
        
        called_filters = {}
        
        class MockMCPClient:
            async def search_vehicle(self, filters):
                called_filters.update(filters)
                return []
        
        monkeypatch.setattr("client.infrastructure.tools.search_vehicle_tool.MCPClient", MockMCPClient)
        
        await tool._arun(brand="Toyota", model=None, color="Azul", price=None)
        
        # Verifica que apenas valores não-None foram enviados
        assert "brand" in called_filters
        assert "color" in called_filters
        assert "model" not in called_filters
        assert "price" not in called_filters
        assert called_filters["brand"] == "Toyota"
        assert called_filters["color"] == "Azul"
    
    def test_run_raises_not_implemented(self):
        """Testa que _run levanta NotImplementedError"""
        tool = SearchVehicleTool()
        
        with pytest.raises(NotImplementedError):
            tool._run()
