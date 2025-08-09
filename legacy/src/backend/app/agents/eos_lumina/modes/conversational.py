# conversational.py
from .base import ModeModule
from ..context import AgentContext

class ConversationalMode(ModeModule):
    """Offers insights and provocations in a semi-dialogue."""
    async def handle_input(self, context: AgentContext):
        self.logger.info(f"Handling direct conversation: {context.last_input}")
        context.response = {
            "dialogue": "That is a profound thought. It reminds me of…"
        }
        return context