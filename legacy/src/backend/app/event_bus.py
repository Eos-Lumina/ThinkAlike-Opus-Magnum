# event_bus.py
"""
Backend Event Bus for ThinkAlike
- Publishes and subscribes to system and agent events
- Logs events for observability and traceability
"""
from typing import Callable, Dict, List, Any
import threading

class EventBus:
    def __init__(self):
        self._subscribers: Dict[str, List[Callable[[Any], None]]] = {}
        self._lock = threading.Lock()
        self._register_default_subscribers()

    def _register_default_subscribers(self):
        # Example: Log all agent actions and system events
        def logging_subscriber(event_data):
            print(f"[EventBus][LOG] Event: {event_data}")
        self.subscribe("agent_action", logging_subscriber)
        self.subscribe("system_event", logging_subscriber)

    def subscribe(self, event_type: str, handler: Callable[[Any], None]):
        with self._lock:
            if event_type not in self._subscribers:
                self._subscribers[event_type] = []
            self._subscribers[event_type].append(handler)

    def unsubscribe(self, event_type: str, handler: Callable[[Any], None]):
        with self._lock:
            if event_type in self._subscribers:
                try:
                    self._subscribers[event_type].remove(handler)
                except ValueError:
                    pass  # Handler not found

    def publish(self, event_type: str, event_data: Any):
        handlers = self._subscribers.get(event_type, [])
        for handler in handlers:
            handler(event_data)
        # Log event (placeholder)
        print(f"Event published: {event_type} | Data: {event_data}")

    def list_subscribers(self, event_type: str) -> List[Callable[[Any], None]]:
        with self._lock:
            return list(self._subscribers.get(event_type, []))

# NOTE: Subscribers should be registered at application startup.
# Demo subscribers in api/pci.py are for local development/testing only.

# Example usage
# bus = EventBus()
# bus.subscribe("agent_action", lambda data: print(f"Agent action: {data}"))
# bus.publish("agent_action", {"agent_id": "eos", "action": "initiate"})
