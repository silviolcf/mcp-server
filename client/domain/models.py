from dataclasses import dataclass
from typing import Optional, Dict, Any, List

@dataclass
class Intent:
    """
    Represents the intent extracted from natural language
    For Example: Search a Vehicle with color filter and AT
    """
    name: str
    parameters: Dict[str, any]

@dataclass
class VechicleFilter:
    """
    Represents the filters which can be applied on vehicle search
    """
    brand: Optional[str]
    model: Optional[str]
    fuel_type: Optional[str]
    manufacture_year: Optional[int]
    color: Optional[str]
    mileage: Optional[int]
    doors: Optional[int]
    transmission: Optional[str]
    ac: Optional[bool]
    price: Optional[float]

@dataclass
class Command:
    """
    Represents a command which will be sended to mcp server
    """
    tool_name: str
    input_data: Dict[str,Any]

@dataclass
class Vechile:
    """
    Represents a vehicle returned by mcp server
    """
    id: int
    brand: str
    model: str
    fuel_type: str
    manufacture_year: int
    color: str
    mileage: int
    doors: int
    transmission: str
    ac: bool
    price: float

@dataclass
class AgentResponse:
    """
    Represents the response to user
    """
    success: bool
    message: str
    data: Optional[List[Vechile]] = None
