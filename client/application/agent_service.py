from client.infrastructure.langchain_prompt import get_agent
from client.domain.models import AgentResponse, Vechile
from typing import List


class AgentService:
    def __init__(self):
        self.agent = get_agent()

    async def run(self, user_input: str) -> AgentResponse:
        try:
            result = await self.agent.ainvoke({"input": user_input})

            if isinstance(result, list) and all(isinstance(vehicle, dict) for vehicle in result):
                vehicles = [Vechile(**vehicle) for vehicle in result]
                return AgentResponse(
                    success=True,
                    message=f"{len(vehicles)} veículos encontrados",
                    data=vehicles
                )
            
            return AgentResponse(success=True, message=str(result))
        
        except Exception as e:
            return AgentResponse(success=False, message=f"Erro: {str(e)}")