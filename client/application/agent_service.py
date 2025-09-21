from client.infrastructure.langchain_prompt import get_agent
from client.domain.models import AgentResponse, Vehicle
from typing import List, Optional
import re


class AgentService:
    def __init__(self):
        self.agent = get_agent()

    def extract_filters_from_history(self, search_history: List[str]) -> dict:
        """Extrai filtros do histórico de buscas para manter contexto"""
        filters = {}
        for search in search_history:

            if "toyota" in search.lower():
                filters["brand"] = "Toyota"
            elif "honda" in search.lower():
                filters["brand"] = "Honda"
            elif "ford" in search.lower():
                filters["brand"] = "Ford"
            

            colors = ["vermelho", "azul", "branco", "preto", "prata", "cinza"]
            for color in colors:
                if color in search.lower():
                    filters["color"] = color.title()
                    break
            

            if "automático" in search.lower() or "automatico" in search.lower():
                filters["transmission"] = "AT"
            elif "manual" in search.lower():
                filters["transmission"] = "MT"
            

            if "ar condicionado" in search.lower() or "ac" in search.lower():
                filters["ac"] = True
        
        return filters

    def generate_suggestion(self, user_input: str, search_history: List[str]) -> Optional[str]:
        """Gera sugestões baseadas na busca atual e histórico"""
        input_lower = user_input.lower()
        

        if "até" in input_lower and "reais" in input_lower:

            price_match = re.search(r'até\s*(\d+)', input_lower)
            if price_match:
                current_price = int(price_match.group(1))
                new_price = current_price * 1.5 
                return f"Buscar carros até {new_price:,.0f} reais"
        

        if "automático" in input_lower and "até" in input_lower:
            return "Buscar carros manuais (geralmente mais baratos)"
        
        if "toyota" in input_lower:
            return "Buscar carros Honda ou Ford (alternativas similares)"
        
        if "vermelho" in input_lower:
            return "Buscar carros azuis ou brancos (cores mais comuns)"
        
        return "Tentar uma busca mais ampla removendo alguns filtros"

    async def run(self, user_input: str, search_history: List[str] = None) -> AgentResponse:
        try:
            if search_history is None:
                search_history = []
            
            result = await self.agent.ainvoke({"input": user_input})

            if isinstance(result, list) and all(isinstance(vehicle, dict) for vehicle in result):
                vehicles = [Vehicle(**vehicle) for vehicle in result]
                
                if vehicles:
                    return AgentResponse(
                        success=True,
                        message=f"{len(vehicles)} veículos encontrados!",
                        data=vehicles
                    )
                else:
                    suggestion = self.generate_suggestion(user_input, search_history)
                    return AgentResponse(
                        success=False,
                        message="Nenhum veículo encontrado com os filtros fornecidos.",
                        suggestion=suggestion
                    )
            
            message = str(result)
            if "não consegui encontrar" in message.lower() or "nenhum" in message.lower():
                suggestion = self.generate_suggestion(user_input, search_history)
                return AgentResponse(
                    success=False,
                    message=message,
                    suggestion=suggestion
                )
            
            return AgentResponse(success=True, message=message)
        
        except Exception as e:
            return AgentResponse(success=False, message=f"Erro: {str(e)}")