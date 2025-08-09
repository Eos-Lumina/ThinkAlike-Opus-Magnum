"""
Canonical Implementation of the Eos Lumina Agent
================================================

This module provides the definitive implementation for the Eos Lumina agent.
It is designed to be persona-driven, loading its core identity, communication
style, and operational parameters directly from a corresponding YAML file.

This approach ensures a clean separation of concerns, where the agent's logic
(this file) is distinct from its personality configuration.

Architecture:
- Loads persona from `agents/core/eos_lumina_persona.yaml`.
- Provides methods for core functions: welcoming, message processing, oracle mode.
- Establishes a foundation for routing to specialized sub-agents.

"""
import yaml
from src.backend.app.event_bus import EventBus
import logging
from pathlib import Path
from typing import Any, Dict, Optional

# Configure basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class EosLuminaAgent:
    """
    Eos Lumina: The primary guiding intelligence for the ThinkAlike ecosystem.

    This agent acts as the initial point of contact, guiding users,
    understanding their intent, and orchestrating responses, either
    directly or by routing to more specialized agents.
    """
    _persona: Dict[str, Any] = {}

    def __init__(self, persona_path: Optional[Path] = None):
        self._event_bus = EventBus()
        """
        Initializes the Eos Lumina agent by loading its persona.

        Args:
            persona_path: The file path to the persona YAML file. If not
                          provided, it defaults to the canonical location.
        """
        if not self._persona:
            self._load_persona(persona_path)

    def _load_persona(self, persona_path: Optional[Path] = None):
        """
        Loads the agent's persona from the canonical YAML file.
        """
        if persona_path:
            canonical_path = persona_path
        else:
            # Assumes this script is in src/backend/app/agents/
            # The path to the project root is four levels up.
            base_dir = Path(__file__).resolve().parents[4]
            canonical_path = base_dir / "src" / "api" / "eos_lumina_persona.yaml"

        logger.info(f"Loading Eos Lumina persona from: {canonical_path}")
        try:
            with open(canonical_path, "r", encoding="utf-8") as f:
                self.__class__._persona = yaml.safe_load(f)
            logger.info("Eos Lumina persona loaded successfully.")
        except FileNotFoundError:
            logger.error(f"CRITICAL: Persona file not found at {canonical_path}. Eos Lumina cannot function.")
            raise
        except yaml.YAMLError as e:
            logger.error(f"CRITICAL: Error parsing persona file: {e}")
            raise

    @property
    def persona(self) -> Dict[str, Any]:
        """Provides access to the loaded persona data."""
        return self._persona

    def welcome(self, user_name: str = "co-architect") -> str:
        """
        Generates a personalized welcome message based on the persona.
        """
        greeting = self.persona.get("communication_style", {}).get("preferred_phrasing", [])[0]
        message = greeting.format(user_name=user_name)
        self._event_bus.publish("agent_welcome", {"agent": "EosLumina", "user": user_name, "message": message})
        return message

    def process_message(self, message: str) -> str:
        """
        Processes an incoming message and determines the appropriate response.

        This is the core logic hub. It will eventually route to sub-agents,
        trigger oracle mode, or generate a direct response.

        Args:
            message: The user's input message.

        Returns:
            A string containing the agent's response.
        """
        # Check for oracle mode triggers
        lower_message = message.lower()
        oracle_triggers = self.persona.get("extended_attributes", {}).get("oracle_mode_definition", {}).get("triggers", [])
        if any(trigger in lower_message for trigger in oracle_triggers):
            response = self.invoke_oracle_mode()
            self._event_bus.publish("agent_oracle_mode", {"agent": "EosLumina", "input": message, "response": response})
            return response
        # Placeholder for sub-agent routing logic
        # For now, return a standard guidance response
        response = self.persona.get("system_prompt_components", {}).get("style_guidance", "How may I guide you?")
        self._event_bus.publish("agent_message_processed", {"agent": "EosLumina", "input": message, "response": response})
        return response

    def invoke_oracle_mode(self) -> str:
        """
        Generates a response in the persona's "Oracle Mode."
        """
        import random
        oracle_def = self.persona.get("extended_attributes", {}).get("oracle_mode_definition", {})
        intro_phrases = oracle_def.get("intro_phrases", ["Consider this..."])
        
        # Combine elements for a structured oracle response
        intro = random.choice(intro_phrases)
        guidance = random.choice(self.persona.get("extended_attributes", {}).get("ritual_directives_process", []))
        response = f"{intro}\n\n{guidance}"
        self._event_bus.publish("agent_oracle_response", {"agent": "EosLumina", "response": response})
        return response

# Example of how to instantiate and use the agent
if __name__ == '__main__':
    try:
        eos_lumina = EosLuminaAgent()
        
        # --- Welcome Message ---
        print("--- Agent Welcome ---")
        print(eos_lumina.welcome())
        print("\n" + "="*20 + "\n")

        # --- Standard Interaction ---
        print("--- Standard Query ---")
        response = eos_lumina.process_message("What is the purpose of this project?")
        print(f"User Query: What is the purpose of this project?")
        print(f"Eos Lumina: {response}")
        print("\n" + "="*20 + "\n")
        
        # --- Oracle Mode Interaction ---
        print("--- Oracle Mode Query ---")
        oracle_response = eos_lumina.process_message("Tell me my destiny.")
        print(f"User Query: Tell me my destiny.")
        print(f"Eos Lumina: {oracle_response}")
        print("\n" + "="*20 + "\n")

    except Exception as e:
        logger.error(f"An error occurred during the example execution: {e}")

