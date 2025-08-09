"""
Central context object for Eos Lumina sessions.
"""

from typing import Optional, Dict

class AgentContext:
    """
    Carries session state, last input, and the response payload.
    """

    def __init__(self, session_id: str, user_id: str, last_input: Optional[dict] = None):
        self.session_id = session_id
        self.user_id = user_id
        self.last_input = last_input
        self.response: Dict = {}
