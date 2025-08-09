from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List, Optional
from ..models.pci_models import PersonaProfile, PCIConsent
from ..db import get_db
from ..event_bus import EventBus

bus = EventBus()

def log_event(event_data):
    print(f"[EventBus] Event received: {event_data}")

# ---
# DEMO: EventBus subscribers below are for local development/testing only.
# In production, register subscribers at application startup in a dedicated module.
# ---
# Subscribe to all PCI-related events for demonstration
bus.subscribe("pci_consent_created", log_event)
bus.subscribe("pci_consent_updated", log_event)
bus.subscribe("pci_consent_deleted", log_event)
bus.subscribe("persona_profile_created", log_event)
bus.subscribe("persona_profile_updated", log_event)
bus.subscribe("persona_profile_deleted", log_event)

router = APIRouter(prefix="/pci", tags=["PCI"])

# Pydantic Schemas
class PCIConsentCreateSchema(BaseModel):
    contributor_id: str
    pci_opt_in: bool
    symbolic_responses_consent: bool
    value_priorities_consent: bool
    narrative_shares_consent: bool
    preference_tags_consent: bool
    consent_version: str
    eos_lumina_session_id: Optional[str] = None
    withdrawal_reason: Optional[str] = None

class PCIConsentSchema(PCIConsentCreateSchema):
    id: str
    consent_timestamp: Optional[str]
    last_updated: Optional[str]
    class Config:
        orm_mode = True

class PersonaProfileCreateSchema(BaseModel):
    contributor_id: str
    consent_id: str
    profile_version: int
    symbolic_responses_count: int
    value_priorities_count: int
    narrative_shares_count: int
    preference_tags_count: int
    eos_lumina_guidance_level: str
    profile_depth: str

class PersonaProfileSchema(PersonaProfileCreateSchema):
    id: str
    profile_creation_date: Optional[str]
    profile_last_modified: Optional[str]
    class Config:
        orm_mode = True

# PCIConsent Endpoints
@router.post("/consent", response_model=PCIConsentSchema)
def create_consent(consent: PCIConsentCreateSchema, db: Session = Depends(get_db)):
    obj = PCIConsent(**consent.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    bus.publish("pci_consent_created", {"id": obj.id, "contributor_id": obj.contributor_id})
    return obj

@router.get("/consent/{contributor_id}", response_model=PCIConsentSchema)
def get_consent(contributor_id: str, db: Session = Depends(get_db)):
    obj = db.query(PCIConsent).filter_by(contributor_id=contributor_id).first()
    if not obj:
        raise HTTPException(status_code=404, detail="Consent not found")
    return obj

@router.put("/consent/{contributor_id}", response_model=PCIConsentSchema)
def update_consent(contributor_id: str, consent: PCIConsentCreateSchema, db: Session = Depends(get_db)):
    obj = db.query(PCIConsent).filter_by(contributor_id=contributor_id).first()
    if not obj:
        raise HTTPException(status_code=404, detail="Consent not found")
    for key, value in consent.dict().items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    bus.publish("pci_consent_updated", {"id": obj.id, "contributor_id": obj.contributor_id})
    return obj

@router.delete("/consent/{contributor_id}")
def delete_consent(contributor_id: str, db: Session = Depends(get_db)):
    obj = db.query(PCIConsent).filter_by(contributor_id=contributor_id).first()
    if not obj:
        raise HTTPException(status_code=404, detail="Consent not found")
    db.delete(obj)
    db.commit()
    bus.publish("pci_consent_deleted", {"id": obj.id, "contributor_id": obj.contributor_id})
    return {"detail": "Consent deleted"}

# PersonaProfile Endpoints
@router.post("/profile", response_model=PersonaProfileSchema)
def create_profile(profile: PersonaProfileCreateSchema, db: Session = Depends(get_db)):
    obj = PersonaProfile(**profile.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    bus.publish("persona_profile_created", {"id": obj.id, "contributor_id": obj.contributor_id})
    return obj

@router.get("/profile/{contributor_id}", response_model=PersonaProfileSchema)
def get_profile(contributor_id: str, db: Session = Depends(get_db)):
    obj = db.query(PersonaProfile).filter_by(contributor_id=contributor_id).first()
    if not obj:
        raise HTTPException(status_code=404, detail="Profile not found")
    return obj

@router.put("/profile/{contributor_id}", response_model=PersonaProfileSchema)
def update_profile(contributor_id: str, profile: PersonaProfileCreateSchema, db: Session = Depends(get_db)):
    obj = db.query(PersonaProfile).filter_by(contributor_id=contributor_id).first()
    if not obj:
        raise HTTPException(status_code=404, detail="Profile not found")
    for key, value in profile.dict().items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    bus.publish("persona_profile_updated", {"id": obj.id, "contributor_id": obj.contributor_id})
    return obj

@router.delete("/profile/{contributor_id}")
def delete_profile(contributor_id: str, db: Session = Depends(get_db)):
    obj = db.query(PersonaProfile).filter_by(contributor_id=contributor_id).first()
    if not obj:
        raise HTTPException(status_code=404, detail="Profile not found")
    db.delete(obj)
    db.commit()
    bus.publish("persona_profile_deleted", {"id": obj.id, "contributor_id": obj.contributor_id})
    return {"detail": "Profile deleted"}

@router.get("/profiles", response_model=List[PersonaProfileSchema])
def list_profiles(db: Session = Depends(get_db)):
    return db.query(PersonaProfile).all()
