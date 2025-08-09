# presence.py
from .base import ModeModule
from ..context import AgentContext

class PresenceMode(ModeModule):
    """Provides ambient awareness and speaks when silence welcomes her."""
    async def handle_input(self, context: AgentContext) -> AgentContext:
        self.logger.info("Considering ambient interjection…")
        context.response = {
            "ambient_cue": "A soft chime sounds in the distance."
        }
        return context