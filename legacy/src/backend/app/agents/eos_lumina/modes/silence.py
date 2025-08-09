# silence.py
from .base import ModeModule
from ..context import AgentContext

class SilenceMode(ModeModule):
    """Expresses presence through intentional absence."""
    async def enter(self, context: AgentContext):
        self.logger.info("Entering SilenceMode. Eos will now be still.")
        context.response = {"system_state": "Eos is silent."}
        return context