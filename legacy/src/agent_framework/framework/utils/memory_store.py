from typing import Any, Dict, List

class MemoryStore:
    """A simple in-memory store for agent memories and contextual data."""
    def __init__(self):
        self._data: Dict[str, Any] = {}

    def set(self, key: str, value: Any):
        """Store a value associated with a key."""
        self._data[key] = value

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieve a value by key. Returns default if key not found."""
        return self._data.get(key, default)

    def delete(self, key: str):
        """Delete a key-value pair."""
        if key in self._data:
            del self._data[key]

    def has(self, key: str) -> bool:
        """Check if a key exists in the store."""
        return key in self._data

    def clear(self):
        """Clear all data from the store."""
        self._data.clear()

    def get_all(self) -> Dict[str, Any]:
        """Retrieve all data from the store."""
        return self._data.copy()

# Example (can be moved to tests or examples)
# if __name__ == "__main__":
#     memory = MemoryStore()
#     memory.set("agent_status", "active")
#     memory.set("last_interaction_timestamp", 1678886400)
#     print(f"Agent status: {memory.get('agent_status')}")
#     print(f"All memory: {memory.get_all()}")
#     memory.delete("agent_status")
#     print(f"Has agent_status: {memory.has('agent_status')}")
#     memory.clear()
#     print(f"Memory after clear: {memory.get_all()}")
