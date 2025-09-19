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
        ("system", "Você é um assistente especializado em busca de veículos. Use a ferramenta 'search_vehicle' para encontrar carros com base nos filtros fornecidos."),
        ("user", "{input}"),
        ("assistant", "{agent_scratchpad}")
    ])


    agent = create_openai_functions_agent(
        tools=[mcp_tool],
        llm=llm, prompt=prompt)
    executor = AgentExecutor(agent=agent, tools=[mcp_tool], verbose=True)


    return executor