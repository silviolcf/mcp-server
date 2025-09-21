from langchain.agents import create_openai_functions_agent,AgentExecutor, initialize_agent, Tool
from langchain.agents.agent_types import AgentType
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from client.infrastructure.openai_service import OpenAIService
from client.infrastructure.tools.search_vehicle_tool import SearchVehicleTool
from .mcp_client import MCPClient

def get_agent():
    llm = OpenAIService().get_model()
    mcp_tool = SearchVehicleTool()

    prompt = ChatPromptTemplate.from_messages([
        ("system", """Você é um assistente especializado em busca de veículos. 
        
        Use a ferramenta 'search_vehicle' para encontrar carros com base nos filtros fornecidos pelo usuário.
        
        Filtros disponíveis:
        - brand: marca do veículo (ex: Toyota, Honda, Ford)
        - model: modelo do veículo (ex: Corolla, Civic, Focus)
        - color: cor do veículo (ex: vermelho, azul, branco)
        - fuel_type: tipo de combustível (ex: Gasolina, Etanol, Flex)
        - manufacture_year: ano de fabricação (ex: 2020, 2021, 2022)
        - mileage: quilometragem máxima (ex: 50000, 100000)
        - doors: número de portas (ex: 2, 4)
        - transmission: tipo de transmissão (ex: Manual, Automático)
        - ac: ar-condicionado (true/false)
        - price: preço máximo (ex: 50000.0, 100000.0)
        
        INSTRUÇÕES IMPORTANTES:
        1. Sempre extraia os filtros relevantes da consulta do usuário e use apenas os filtros que foram mencionados.
        2. Se encontrar veículos, apresente-os de forma clara e organizada.
        3. Se NENHUM veículo for encontrado, responda de forma educada e sugira alternativas específicas como:
           - Aumentar o orçamento em 20-50%
           - Considerar marcas similares
           - Remover filtros muito restritivos
           - Sugerir cores mais comuns
        4. Seja sempre prestativo e ofereça opções práticas para o usuário.
        
        Exemplo de resposta quando não encontrar veículos:
        "Desculpe, não encontrei veículos com esses critérios específicos. Que tal tentar:
        - Aumentar o orçamento para R$ 75.000
        - Considerar carros manuais (geralmente mais baratos)
        - Buscar por cores mais comuns como branco ou prata"
        """),
        ("user", "{input}"),
        ("assistant", "{agent_scratchpad}")
    ])


    agent = create_openai_functions_agent(
        tools=[mcp_tool],
        llm=llm, prompt=prompt)
    executor = AgentExecutor(agent=agent, tools=[mcp_tool], verbose=True)


    return executor