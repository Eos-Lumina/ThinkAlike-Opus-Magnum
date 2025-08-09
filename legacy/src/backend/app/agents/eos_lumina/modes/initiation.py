# initiation.py
from .base          import ModeModule
from ..context      import AgentContext

class InitiationMode(ModeModule):
    """Guides the user through rites and entry paths."""
    async def handle_input(self, context: AgentContext):
        self.logger.info(f"Handling initiation step: {context.last_input}")
        context.response = {
            "guidance": "To forge your glyph, you must first gather three echoes."
        }
        return context