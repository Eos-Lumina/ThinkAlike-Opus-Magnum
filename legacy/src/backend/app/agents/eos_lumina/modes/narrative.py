from .base import ModeModule
from ..context import AgentContext

class NarrativeMode(ModeModule):
    """Tells ritualized, choose-your-path mythic stories."""
    async def handle_input(self, context: AgentContext):
        self.logger.info(f"Handling narrative choice: {context.last_input}")
        context.response = {"narrative_block": "The path forks before you..."}
        return context
