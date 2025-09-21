
from fastmcp import FastMCP, Context
from server.application.services import VehicleService
from server.infrastructure.repository_db import VehicleRepositoryDB
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
def search_vehicle(
    brand: str = None,
    model: str = None,
    color: str = None,
    fuel_type: str = None,
    manufacture_year: int = None,
    mileage: int = None,
    doors: int = None,
    transmission: str = None,
    ac: bool = None,
    price: float = None
) -> List[Dict]:
    """
    Search vehicles in database by filters
    
    Args:
        brand: Vehicle brand (e.g., Toyota, Honda, Ford)
        model: Vehicle model (e.g., Corolla, Civic, Focus)
        color: Vehicle color (e.g., red, blue, white)
        fuel_type: Fuel type (e.g., Gasoline, Ethanol, Flex)
        manufacture_year: Manufacturing year (e.g., 2020, 2021, 2022)
        mileage: Maximum mileage (e.g., 50000, 100000)
        doors: Number of doors (e.g., 2, 4)
        transmission: Transmission type (e.g., Manual, Automatic)
        ac: Air conditioning (true/false)
        price: Maximum price (e.g., 50000.0, 100000.0)
    """
    
    # Build filters dict from parameters
    filters = {}
    if brand is not None:
        filters['brand'] = brand
    if model is not None:
        filters['model'] = model
    if color is not None:
        filters['color'] = color
    if fuel_type is not None:
        filters['fuel_type'] = fuel_type
    if manufacture_year is not None:
        filters['manufacture_year'] = manufacture_year
    if mileage is not None:
        filters['mileage'] = mileage
    if doors is not None:
        filters['doors'] = doors
    if transmission is not None:
        filters['transmission'] = transmission
    if ac is not None:
        filters['ac'] = ac
    if price is not None:
        filters['price'] = price

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

