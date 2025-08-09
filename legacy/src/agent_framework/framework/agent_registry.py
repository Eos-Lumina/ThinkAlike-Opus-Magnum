from typing import Dict, Type
from .base_agent import BaseAgent

class AgentRegistry:
    def __init__(self):
        self._agents: Dict[str, Type[BaseAgent]] = {}

    def register_agent(self, agent_class: Type[BaseAgent]):
        if not hasattr(agent_class, 'agent_type') or not agent_class.agent_type:
            raise ValueError("Agent class must have an 'agent_type' attribute.")
        self._agents[agent_class.agent_type] = agent_class

    def get_agent_class(self, agent_type: str) -> Type[BaseAgent] | None:
        return self._agents.get(agent_type)

    def list_registered_agents(self) -> list[str]:
        return list(self._agents.keys())

# Global instance (optional, can be managed by a central service)
agent_registry = AgentRegistry()

def register_agent(agent_class: Type[BaseAgent]):
    agent_registry.register_agent(agent_class)

def get_agent_class(agent_type: str) -> Type[BaseAgent] | None:
    return agent_registry.get_agent_class(agent_type)
