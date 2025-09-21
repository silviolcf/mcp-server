import pytest
from client.infrastructure.mcp_client import MCPClient

def test_mcp_client_initialization():
    """Testa inicialização do cliente MCP"""
    client = MCPClient("http://localhost:8000/mcp")
    
    assert client.server_url == "http://localhost:8000/mcp"

def test_mcp_client_default_url():
    """Testa inicialização com URL padrão"""
    client = MCPClient()
    
    assert client.server_url == "http://localhost:8000/mcp"
