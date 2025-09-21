import asyncio
import os
from client.application.agent_service import AgentService
from client.infrastructure.mcp_client import MCPClient
from tabulate import tabulate
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich import box


async def format_vehicle_table(vehicles):
    """Formata a tabela de veículos com Rich para melhor apresentação"""
    console = Console()
    
    # Cria tabela com Rich
    table = Table(
        title="Veículos Encontrados",
        box=box.ROUNDED,
        show_header=True,
        header_style="bold blue",
        title_style="bold green"
    )
    
    # Adiciona colunas
    table.add_column("ID", style="dim", width=4)
    table.add_column("Marca", style="cyan", width=12)
    table.add_column("Modelo", style="magenta", width=12)
    table.add_column("Cor", style="yellow", width=10)
    table.add_column("Ano", style="green", width=6)
    table.add_column("Preço", style="bold red", width=15)
    table.add_column("Transmissão", style="blue", width=12)
    table.add_column("AC", style="green", width=4)
    table.add_column("Portas", style="dim", width=6)
    table.add_column("Combustível", style="yellow", width=10)
    table.add_column("Km", style="dim", width=8)
    
    # Adiciona dados
    for vehicle in vehicles:
        table.add_row(
            str(vehicle.id),
            vehicle.brand,
            vehicle.model,
            vehicle.color,
            str(vehicle.manufacture_year),
            f"R$ {vehicle.price:,.2f}",
            vehicle.transmission,
            "Sim" if vehicle.ac else "Não",
            str(vehicle.doors),
            vehicle.fuel_type,
            f"{vehicle.mileage:,} km"
        )
    
    console.print(table)
    return len(vehicles)


async def wait_for_server():
    """Aguarda o servidor MCP ficar disponível"""
    console = Console()
    mcp = MCPClient()
    
    console.print("[yellow]Aguardando servidor...[/yellow]")
    
    max_attempts = 30
    attempt = 0
    
    while attempt < max_attempts:
        try:
            await mcp.get_welcome_prompt()
            console.print("[green]Servidor conectado![/green]")
            return True
        except Exception:
            attempt += 1
            await asyncio.sleep(2)
            if attempt % 5 == 0:  # A cada 10 segundos
                console.print(f"[yellow]Tentativa {attempt}/{max_attempts}...[/yellow]")
    
    console.print("[red]Não foi possível conectar ao servidor[/red]")
    return False


async def main():
    console = Console()
    
    welcome_panel = Panel(
        Text("MCP Vehicle Search Assistant", style="bold green"),
        subtitle="Sistema inteligente de busca de veículos",
        border_style="green"
    )
    console.print(welcome_panel)

    if not await wait_for_server():
        return
    
    console.print("[green]Iniciando cliente...[/green]")
    
    mcp = MCPClient()
    welcome = await mcp.get_welcome_prompt()
    
    agent = AgentService()
    console.print(f"\n[bold blue]{welcome}[/bold blue]")
    
    search_history = []
    
    while True:
        user_input = input("\nDigite sua busca: ")
        if user_input.lower() in ["sair", "quit", "exit"]:
            console.print("\n[bold green]Obrigado, volte sempre![/bold green]")
            break

        search_history.append(user_input)
        
        response = await agent.run(user_input, search_history)

        if response.suggestion:
            suggestion_panel = Panel(
                f"[bold yellow]Sugestão:[/bold yellow] {response.suggestion}",
                border_style="yellow"
            )
            console.print(suggestion_panel)
            
            apply_suggestion = input("\nAplicar esta sugestão? (s/n): ").lower().strip()
            if apply_suggestion in ['s', 'sim', 'y', 'yes']:
                suggestion_response = await agent.run(response.suggestion, search_history)
                if suggestion_response.data:
                    await format_vehicle_table(suggestion_response.data)
                continue

        if response.data:
            await format_vehicle_table(response.data)


if __name__ == "__main__":
    asyncio.run(main())
