# oracle.py
from .base import ModeModule
from ..context import AgentContext

class OracleMode(ModeModule):
    """Answers paradoxes with cryptic clarity."""
    async def handle_input(self, context: AgentContext):
        self.logger.info(f"Handling oracle query: {context.last_input}")
        context.response = {
            "oracle_text": "The branch that bends is the one that does not break."
        }
        return context
