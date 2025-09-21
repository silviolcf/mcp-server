from langchain.tools import BaseTool
from typing import Optional, Any
from client.infrastructure.mcp_client import MCPClient
from client.domain.models import VehicleFilter
from client.domain.schemas import VehicleFilterSchema

class SearchVehicleTool(BaseTool):
    name:str = "search_vehicle"
    description:str = (
        "Busca veículos em uma base de dados. "
        "Você pode filtrar por marca, modelo, cor, tipo de combustível, ano de fabricação, "
        "quilometragem, número de portas, transmissão, ar-condicionado e preço. "
        "Use as seguintes chaves em inglês: brand, model, manufacture_year, fuel_type, color, "
        "mileage, doors, transmission, ac (boolean), price. "
        "Exemplo: search_vehicle({\"brand\": \"Toyota\", \"color\": \"vermelho\"})"
    )
    args_schema: type = VehicleFilterSchema

    def __init__(self):
        super().__init__()

    async def _arun(self, **kwargs) -> Any:
        filters = {k: v for k, v in kwargs.items() if v is not None}
        client = MCPClient()
        return await client.search_vehicle(filters)

    def _run(self, *args, **kwargs):
        raise NotImplementedError("Use assincronous version with await.")