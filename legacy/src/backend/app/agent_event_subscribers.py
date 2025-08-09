"""
Agent Event Subscribers for ThinkAlike
- Register event bus subscribers for agent actions and system events
- Extend for custom agent workflows, logging, and orchestration
"""
from .event_bus import EventBus

bus = EventBus()

def log_agent_action(event_data):
    print(f"[AgentEvent] Action: {event_data}")

def log_system_event(event_data):
    print(f"[SystemEvent] Event: {event_data}")

def log_value_profile_event(event_data):
    print(f"[ValueProfileEvent] {event_data}")

# Register subscribers for agent actions and system events
bus.subscribe("agent_action", log_agent_action)
bus.subscribe("system_event", log_system_event)

# Register subscribers for value profile events
bus.subscribe("value_profile_created", log_value_profile_event)
bus.subscribe("value_profile_updated", log_value_profile_event)
bus.subscribe("value_profile_deleted", log_value_profile_event)

# Extend with additional subscribers as needed
