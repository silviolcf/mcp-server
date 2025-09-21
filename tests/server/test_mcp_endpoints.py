import pytest
from server.interface.mcp_server import mcp

def test_mcp_server_initialization():
    """Testa se o servidor MCP foi inicializado corretamente"""
    assert mcp is not None
    assert hasattr(mcp, 'name')
    assert mcp.name == "Mcp Vehicles"

def test_mcp_server_has_methods():
    """Testa se o servidor tem métodos básicos"""
    # Verifica se tem métodos básicos do FastMCP
    assert hasattr(mcp, 'add_resource')
    assert hasattr(mcp, 'add_tool')
