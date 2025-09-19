import asyncio
from client.application.agent_service import AgentService
from client.infrastructure.mcp_client import MCPClient
from tabulate import tabulate


async def main():
    print("Mcp Vehicle started")

    mcp = MCPClient()
    welcome = await mcp.get_welcome_prompt()
    
    agent = AgentService()
    print(f"\n {welcome}")
    while True:
        user_input = input("")
        if user_input.lower() in ["sair", "quit", "exit"]:
            print("Obrigado, volte sempre!")
            break

        response = await agent.run(user_input)

        print(f"\n {response.message}")
        if response.data:
            table = [
                [
                    vehicle.brand,
                    vehicle.model,
                    vehicle.color,
                    vehicle.manufacture_year,
                    f"R$: {vehicle.price:,.2f}",
                    vehicle.transmission,
                    "Sim" if vehicle.ac else "Não",
                    vehicle.doors,
                    vehicle.fuel_type,
                    f"{vehicle.mileage} Km"
                ]
                for vehicle in response.data
            ]

            headers = [
                "Marca", "Modelo", "Cor", "Ano", "Preço",
                "Transmissão", "Ar-condicionado", "Portas",
                "Combustível", "Quilometragem"
            ]

            print("\n Veículos Encontrados")
            print(tabulate(table, headers, tablefmt="grid"))
        else:
            print("Nenhum veículo encontrado com os filtros fornecidos.")


if __name__ == "__main__":
    asyncio.run(main())
