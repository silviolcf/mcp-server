
from fastmcp import FastMCP, Context
from application.services import VehicleService
from infrastructure.repository_db import VehicleRepositoryDB
from typing import List, Dict
import sys


mcp = FastMCP(name="Mcp Vehicles")
vehicle_service = VehicleService(VehicleRepositoryDB())


@mcp.resource("resource://about")
def get_mcp_capabilities() -> str:
    """
    Agent to search vehicles in a database
    """
    print("-> Resource 'mcpVehicles://about' requested from client.")
    capabilites = """
    Eu sou um assistente baseado no servidor MCP Vehicles com capacidade de buscar veículos dentro de uma base de dados
    Utilize-me sempre que quiser achar o veículo ideal para você.
    """
    print("[mcpVehicles://about] return capabilities")
    return capabilites.strip()


@mcp.tool()
def search_vehicle(filters: dict) -> List[Dict]:
    """
    #Search vehicles in database by filters
    """

    results = vehicle_service.search_by_filter(filters)

    return [{
        "id": vehicle.id,
        "brand": vehicle.brand,
        "model": vehicle.model,
        "fuel_type": vehicle.fuel_type,
        "manufacture_year": vehicle.manufacture_year,
        "color": vehicle.color,
        "mileage": vehicle.mileage,
        "doors": vehicle.doors,
        "transmission": vehicle.transmission,
        "ac": vehicle.ac,
        "price": vehicle.price
        } 
        for vehicle in results 
    ]

@mcp.prompt()
def welcome_prompt(ctx: Context) -> str:
    print("Prompt chamado!", flush=True)
    return "Olá, me diga o tipo de carro que procura e eu te ajudarei a encontrar"

