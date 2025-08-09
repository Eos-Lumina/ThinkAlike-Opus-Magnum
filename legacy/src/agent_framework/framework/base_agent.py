class BaseAgent:
    def __init__(self, name: str, agent_type: str, specialty: str = "general", description: str = ""):
        self.id = name # Simplified ID for now
        self.name = name
        self.agent_type = agent_type
        self.specialty = specialty
        self.description = description
        self.status = "initialized"

    def process_message(self, collaborator_id: str, message: str, context: dict = None) -> str:
        raise NotImplementedError("Subclasses must implement process_message")

    def evaluate_relevance(self, message: str, context: dict = None) -> float:
        # Placeholder: Subclasses should implement more sophisticated relevance evaluation
        return 0.0 

    def is_available(self) -> bool:
        # Placeholder: Subclasses can implement more complex availability checks
        return self.status == "active"

    def activate(self):
        self.status = "active"
        # Placeholder for activation logic
        pass

    def deactivate(self):
        self.status = "inactive"
        # Placeholder for deactivation logic
        pass
