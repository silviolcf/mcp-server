import asyncio
from fastmcp import Client

class MCPClient:
    def __init__(self, server_url: str = "http://localhost:8000/mcp"):
        self.server_url = server_url

    async def search_vehicle(self, filters:dict):
        async with Client(self.server_url) as client:
            result = await client.call_tool("search_vehicle", filters)
            return [item for item in result.content[0].text]
        
    async def get_capabilities(self):
        async with Client(self.server_url) as client:
            result = await client.read_resource("resource://about")
            return result.text.strip()
        
    async def get_welcome_prompt(self):
        async with Client(self.server_url) as client:
            result = await client.get_prompt("welcome_prompt")
            return result.messages[0].content.text