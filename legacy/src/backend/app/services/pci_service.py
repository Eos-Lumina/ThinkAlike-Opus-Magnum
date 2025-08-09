# Persona Calibration Initiative - API Services
# ...rescued and harmonized from legacy canonical source...

from typing import Dict, List, Optional, Tuple
from datetime import datetime, timezone
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
import uuid
import json

from src.backend.app.models.pci_models import (
    PCIConsent, PCIConsentHistory, TestPersonaProfile, SymbolicResponse,
    ValuePriority, NarrativeShare, PreferenceTag, AlgorithmTestUsage,
    PCIDashboardSession, EosLuminaPCISession, AlgorithmTestFeedback
)
from src.backend.app.schemas.pci_schemas import (
    PCIConsentCreate, PCIConsentUpdate, TestPersonaProfileCreate,
    SymbolicResponseCreate, ValuePriorityCreate, NarrativeShareCreate,
    PreferenceTagCreate, PCIConsentResponse, TestPersonaProfileResponse
)

class PCIService:
    def __init__(self, db: Session):
        self.db = db
    # ...full implementation as in canonical legacy source...
