from typing import List, Dict, Any, Optional
from datetime import datetime

class Message:
    def __init__(self, sender_id: str, content: str, timestamp: Optional[datetime] = None, metadata: Optional[Dict[str, Any]] = None):
        self.sender_id = sender_id
        self.content = content
        self.timestamp = timestamp or datetime.utcnow()
        self.metadata = metadata or {}

    def __repr__(self):
        return f"Message(sender='{self.sender_id}', content='{self.content[:50]}...', timestamp='{self.timestamp}')"

class ConversationContext:
    """Manages the history and context of a conversation."""
    def __init__(self, context_id: str, initial_context: Optional[Dict[str, Any]] = None):
        self.context_id = context_id
        self.history: List[Message] = []
        self.metadata: Dict[str, Any] = initial_context or {}
        self.custom_attributes: Dict[str, Any] = {}

    def add_message(self, sender_id: str, content: str, metadata: Optional[Dict[str, Any]] = None):
        """Adds a message to the conversation history."""
        message = Message(sender_id, content, metadata=metadata)
        self.history.append(message)

    def get_history(self, limit: Optional[int] = None) -> List[Message]:
        """Returns the conversation history, optionally limited to the most recent messages."""
        if limit:
            return self.history[-limit:]
        return self.history

    def set_metadata(self, key: str, value: Any):
        """Sets a metadata attribute for the conversation."""
        self.metadata[key] = value

    def get_metadata(self, key: str, default: Any = None) -> Any:
        """Gets a metadata attribute."""
        return self.metadata.get(key, default)
    
    def set_attribute(self, key: str, value: Any):
        """Sets a custom attribute for the conversation context."""
        self.custom_attributes[key] = value

    def get_attribute(self, key: str, default: Any = None) -> Any:
        """Gets a custom attribute."""
        return self.custom_attributes.get(key, default)

    def clear_history(self):
        """Clears the conversation history."""
        self.history = []

    def __repr__(self):
        return f"ConversationContext(id='{self.context_id}', messages={len(self.history)})"

# Example (can be moved to tests or examples)
# if __name__ == "__main__":
#     convo = ConversationContext("chat123", initial_context={"topic": "AI safety"})
#     convo.add_message("user_A", "Hello, what are your thoughts on AI alignment?")
#     congo.add_message("agent_B", "AI alignment is a critical area of research...")
#     convo.set_attribute("urgency", "high")

#     print(convo)
#     for msg in convo.get_history():
#         print(f"  {msg.sender_id}: {msg.content}")
#     print(f"Topic: {convo.get_metadata('topic')}")
#     print(f"Urgency: {convo.get_attribute('urgency')}")
