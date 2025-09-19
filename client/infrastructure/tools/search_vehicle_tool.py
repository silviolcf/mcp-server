from langchain.tools import BaseTool
from typing import Optional, Any
from client.infrastructure.mcp_client import MCPClient
from client.domain.models import VechicleFilter
from client.domain.schemas import VehicleFilterSchema, FilterWrapper

class SearchVehicleTool(BaseTool):
    name:str = "search_vehicle"
    description:str = (
        "Busca veículos em uma base de dados. "
        "Você pode filtrar por marca, modelo, cor, tipo de combustível, ano de fabricação, "
        "quilometragem, número de portas, transmissão, ar-condicionado e preço."
        "O dicionário deve seguir as palavras em ingles como: brand, model, manufacture_year, fuel_type, color, mileage,doors,transmission, ac (bool), price"
        "Use a ferramenta 'search_vehicle' passando os filtros dentro do campo `filters`, por exemplo: search_vehicle({\"filters\": {{\"brand\": \"Toyota\"}}}}})"
    )
    args_schema: type = FilterWrapper

    def __init__(self):
        super().__init__()

    async def _arun(self, filters: dict, **kwargs) -> Any:
        client = MCPClient()
        return await client.search_vehicle(filters)

    def _run(self, *args, **kwargs):
        raise NotImplementedError("Use assincronous version with awayt`.")