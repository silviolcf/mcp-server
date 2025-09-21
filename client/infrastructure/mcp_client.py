import asyncio
import os
from fastmcp import Client

class MCPClient:
    def __init__(self, server_url: str = None):
        if server_url is None:
            server_url = os.getenv("MCP_SERVER_URL", "http://localhost:8000/mcp")
        self.server_url = server_url

    async def search_vehicle(self, filters: dict):
        try:
            async with Client(self.server_url) as client:
                result = await client.call_tool("search_vehicle", filters)
                if result.content and len(result.content) > 0:
                    if hasattr(result.content[0], 'text'):
                        import json
                        try:
                            return json.loads(result.content[0].text)
                        except json.JSONDecodeError:
                            return []
                    elif isinstance(result.content[0], list):
                        return result.content[0]
                return []
        except Exception as e:
            print(f"Erro ao buscar veículos: {e}")
            return []
        
    async def get_capabilities(self):
        async with Client(self.server_url) as client:
            result = await client.read_resource("resource://about")
            return result.text.strip()
        
    async def get_welcome_prompt(self):
        async with Client(self.server_url) as client:
            result = await client.get_prompt("welcome_prompt")
            return result.messages[0].content.text