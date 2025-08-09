import pytest
from src.backend.app.event_bus import EventBus

def test_event_bus_publish_and_subscribe():
    bus = EventBus()
    received = []
    def handler(event):
        received.append(event)
    bus.subscribe("test_event", handler)
    bus.publish("test_event", {"msg": "hello"})
    assert received == [{"msg": "hello"}]

def test_event_bus_unsubscribe():
    bus = EventBus()
    received = []
    def handler(event):
        received.append(event)
    bus.subscribe("test_event", handler)
    bus.unsubscribe("test_event", handler)
    bus.publish("test_event", {"msg": "should not be received"})
    assert received == []

def test_event_bus_list_subscribers():
    bus = EventBus()
    def handler(event):
        pass
    bus.subscribe("test_event", handler)
    subs = bus.list_subscribers("test_event")
    assert handler in subs

def test_event_bus_logging_subscriber(capsys):
    bus = EventBus()
    # Publish agent_action event
    bus.publish("agent_action", {"agent_id": "eos", "action": "initiate"})
    # Publish system_event
    bus.publish("system_event", {"system": "ThinkAlike", "status": "started"})
    captured = capsys.readouterr()
    assert "[EventBus][LOG] Event: {'agent_id': 'eos', 'action': 'initiate'}" in captured.out
    assert "[EventBus][LOG] Event: {'system': 'ThinkAlike', 'status': 'started'}" in captured.out
