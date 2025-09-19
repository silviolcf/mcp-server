import asyncio
from fastmcp import Client


client = Client("http://localhost:8000/mcp")

async def call_tool():
    payload = {"brand":"Toyota"}
    async with client:
        result = await client.call_tool("search_vehicle", {"filters":payload})
        print(result.content[0].text)

async def get_prompt():
    async with client:
        result = await client.get_prompt("welcome_prompt")
        print(result.messages[0].content.text)

asyncio.run(get_prompt())
asyncio.run(call_tool())
