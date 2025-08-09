from typing import List, Optional
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from src.backend.app.crud.base import CRUDBase
from src.backend.app.models.value_profile import ValueProfile
from src.backend.app.schemas.value_profile import ValueProfileCreate, ValueProfileUpdate

# EventBus integration: Publishes events for create, update, and delete actions to support observability and event-driven workflows.
from src.backend.app.event_bus import EventBus

bus = EventBus()

class CRUDValueProfile(CRUDBase[ValueProfile, ValueProfileCreate, ValueProfileUpdate]):
    def get_multi_by_user(self, db: Session, *, user_id: int, skip: int = 0, limit: int = 100) -> List[ValueProfile]:
        return (
            db.query(self.model)
            .filter(ValueProfile.user_id == user_id)
            .offset(skip)
            .limit(limit)
            .all()
        )

    def create(self, db: Session, *, obj_in: ValueProfileCreate) -> ValueProfile:
        obj = super().create(db, obj_in=obj_in)
        bus.publish("value_profile_created", jsonable_encoder(obj))
        return obj

    def update(self, db: Session, *, db_obj: ValueProfile, obj_in: ValueProfileUpdate) -> ValueProfile:
        obj = super().update(db, db_obj=db_obj, obj_in=obj_in)
        bus.publish("value_profile_updated", jsonable_encoder(obj))
        return obj

    def remove(self, db: Session, *, id: int) -> Optional[ValueProfile]:
        obj = super().remove(db, id=id)
        if obj:
            bus.publish("value_profile_deleted", jsonable_encoder(obj))
        return obj

value_profile = CRUDValueProfile(ValueProfile)

# TODO: Implement automated tests for event publishing and subscriber invocation for value profile events.
