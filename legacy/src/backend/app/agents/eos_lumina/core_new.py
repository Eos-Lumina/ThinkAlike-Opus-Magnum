import logging
from typing import Dict

from .context                 import AgentContext
from .modes.narrative         import NarrativeMode
from .modes.presence          import PresenceMode
from .modes.conversational    import ConversationalMode
from .modes.initiation        import InitiationMode
from .modes.oracle            import OracleMode
from .modes.silence           import SilenceMode

class EosCore:
    """
    The central "mind" of Eos Lumina, implemented as a hierarchical state machine.
    """
    def __init__(self):
        self.sessions: Dict[str, str] = {}
        self.modes = {
            "NarrativeMode":     NarrativeMode(self),
            "PresenceMode":      PresenceMode(self),
            "ConversationalMode": ConversationalMode(self),
            "InitiationMode":    InitiationMode(self),
            "OracleMode":        OracleMode(self),
            "SilenceMode":       SilenceMode(self),
        }
        self.logger = logging.getLogger("EosCore")
        self.logger.info("EosCore initialized with all mode modules.")

    def get_session_mode(self, session_id: str):
        mode_name = self.sessions.get(session_id, "PresenceMode")
        return self.modes[mode_name]

    async def transition_mode(self, context: AgentContext, new_mode_name: str):
        current = self.get_session_mode(context.session_id)
        new = self.modes[new_mode_name]
        if current is not new:
            await current.exit(context)
            self.sessions[context.session_id] = new_mode_name
            await new.enter(context)
        return context

    async def handle_event(self, event_type: str, context: AgentContext):
        current = self.get_session_mode(context.session_id)

        # Universal trigger: direct user speech
        if event_type == "user_speaks":
            context = await self.transition_mode(context, "ConversationalMode")
            return await self.get_session_mode(context.session_id).handle_input(context)

        # Example: from InitiationMode to PresenceMode
        if isinstance(current, InitiationMode) and event_type == "rite_completed":
            await self.transition_mode(context, "PresenceMode")
            return context

        # Example: from ConversationalMode to OracleMode
        if isinstance(current, ConversationalMode) and event_type == "user_asks_oracle_question":
            context = await self.transition_mode(context, "OracleMode")
            return await self.get_session_mode(context.session_id).handle_input(context)

        # Example: from ConversationalMode to SilenceMode
        if isinstance(current, ConversationalMode) and event_type == "user_says_goodbye":
            await self.transition_mode(context, "SilenceMode")
            return context

        # Default: let current mode handle it
        return await current.handle_input(context)

# Singleton instance to be used by the FastAPI app
eos_core = EosCore()
