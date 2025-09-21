import pytest
from client.application.agent_service import AgentService
from client.domain.models import AgentResponse, Vehicle

class TestAgentService:
    
    def test_generate_suggestion_for_price(self):
        """Testa geração de sugestão baseada em preço"""
        service = AgentService()
        
        suggestion = service.generate_suggestion("Quero um carro até 30000 reais", [])
        
        assert suggestion is not None
        assert "45000" in suggestion or "45000" in suggestion.replace(",", "")
    
    def test_generate_suggestion_for_transmission(self):
        """Testa geração de sugestão baseada em transmissão"""
        service = AgentService()
        
        suggestion = service.generate_suggestion("Quero um carro automático até 40000 reais", [])
        
        assert suggestion is not None
        assert "manual" in suggestion.lower() or "60000" in suggestion.replace(",", "")
    
    def test_generate_suggestion_for_brand(self):
        """Testa geração de sugestão baseada em marca"""
        service = AgentService()
        
        suggestion = service.generate_suggestion("Quero um Toyota", [])
        
        assert suggestion is not None
        assert "honda" in suggestion.lower() or "ford" in suggestion.lower()
    
    def test_extract_filters_from_history(self):
        """Testa extração de filtros do histórico"""
        service = AgentService()
        
        history = [
            "Quero um Toyota vermelho",
            "Com ar condicionado",
            "Automático"
        ]
        
        filters = service.extract_filters_from_history(history)
        
        assert filters["brand"] == "Toyota"
        assert filters["color"] == "Vermelho"
        assert filters["ac"] == True
        assert filters["transmission"] == "AT"
    
    def test_generate_suggestion_generic(self):
        """Testa geração de sugestão genérica"""
        service = AgentService()
        
        suggestion = service.generate_suggestion("Quero um carro", [])
        
        assert suggestion is not None
        assert len(suggestion) > 0
