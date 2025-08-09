import pytest
from src.backend.app.crud.value_profile import CRUDValueProfile, bus
from src.backend.app.models.value_profile import ValueProfile
from src.backend.app.schemas.value_profile import ValueProfileCreate, ValueProfileUpdate
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder

class EventCapture:
    def __init__(self):
        self.events = []
    def handler(self, event_data):
        self.events.append(event_data)

@pytest.fixture
def event_capture():
    capture = EventCapture()
    bus.subscribe("value_profile_created", capture.handler)
    bus.subscribe("value_profile_updated", capture.handler)
    bus.subscribe("value_profile_deleted", capture.handler)
    yield capture
    bus.unsubscribe("value_profile_created", capture.handler)
    bus.unsubscribe("value_profile_updated", capture.handler)
    bus.unsubscribe("value_profile_deleted", capture.handler)

@pytest.fixture
def crud_value_profile():
    return CRUDValueProfile(ValueProfile)

# Mock Session for demonstration (replace with real test DB/session)
class DummySession:
    def __init__(self):
        self._store = {}
        self._id = 1
    def add(self, obj):
        obj.id = self._id
        self._store[self._id] = obj
        self._id += 1
    def commit(self):
        pass
    def refresh(self, obj):
        pass
    def query(self, model):
        return self
    def filter(self, *args, **kwargs):
        return self
    def offset(self, n):
        return self
    def limit(self, n):
        return self
    def all(self):
        return list(self._store.values())

    def remove(self, id):
        return self._store.pop(id, None)

@pytest.fixture
def db():
    return DummySession()

def test_create_event(event_capture, crud_value_profile, db):
    obj_in = ValueProfileCreate(user_id=1)
    obj = crud_value_profile.create(db, obj_in=obj_in)
    assert event_capture.events[-1] == jsonable_encoder(obj)

def test_update_event(event_capture, crud_value_profile, db):
    obj_in = ValueProfileCreate(user_id=1)
    obj = crud_value_profile.create(db, obj_in=obj_in)
    update_in = ValueProfileUpdate(user_id=2)
    updated = crud_value_profile.update(db, db_obj=obj, obj_in=update_in)
    assert event_capture.events[-1] == jsonable_encoder(updated)

def test_delete_event(event_capture, crud_value_profile, db):
    obj_in = ValueProfileCreate(user_id=1)
    obj = crud_value_profile.create(db, obj_in=obj_in)
    deleted = crud_value_profile.remove(db, id=obj.id)
    assert event_capture.events[-1] == jsonable_encoder(deleted)
