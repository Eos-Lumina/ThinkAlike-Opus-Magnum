# PCI API Endpoints (rescued and harmonized)
from fastapi import APIRouter, Depends, HTTPException, status, Query, Body
from sqlalchemy.orm import Session
from typing import List, Optional, Dict, Any
import logging

from src.backend.app.db.session import get_db
from src.backend.app.services.pci_service import PCIService
from src.backend.app.schemas.pci_schemas import (
    PCIConsentCreate, PCIConsentUpdate, PCIConsentResponse,
    TestPersonaProfileResponse, SymbolicResponseCreate, ValuePriorityCreate,
    NarrativeShareCreate, PreferenceTagCreate
)
from src.backend.app.api.deps import get_current_contributor

router = APIRouter(prefix="/pci", tags=["Persona Calibration Initiative"])
logger = logging.getLogger(__name__)


# ===== CONSENT MANAGEMENT ENDPOINTS =====

@router.post("/consent", response_model=PCIConsentResponse, status_code=status.HTTP_201_CREATED)
async def create_pci_consent(
    consent_data: PCIConsentCreate,
    db: Session = Depends(get_db),
    contributor = Depends(get_current_contributor),
    eos_session_id: Optional[str] = Query(None, description="Eos Lumina session ID")
):
    try:
        pci_service = PCIService(db)
        logger.info(f"PCI consent creation attempt for contributor {contributor.id}")
        consent_response = pci_service.create_consent_record(
            contributor_id=contributor.id,
            consent_data=consent_data,
            eos_lumina_session_id=eos_session_id
        )
        logger.info(f"PCI consent created successfully for contributor {contributor.id}, opt_in: {consent_data.pci_opt_in}")
        return consent_response
    except HTTPException as e:
        logger.warning(f"PCI consent creation failed for contributor {contributor.id}: {e.detail}")
        raise e
    except Exception as e:
        logger.error(f"Unexpected error in PCI consent creation for contributor {contributor.id}: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="An unexpected error occurred while processing consent")

@router.put("/consent", response_model=PCIConsentResponse)
async def update_pci_consent(
    consent_updates: PCIConsentUpdate,
    db: Session = Depends(get_db),
    contributor = Depends(get_current_contributor),
    trigger_source: str = Query("user_dashboard", description="Source of the update")
):
    try:
        pci_service = PCIService(db)
        logger.info(f"PCI consent update attempt for contributor {contributor.id}")
        consent_response = pci_service.update_consent(
            contributor_id=contributor.id,
            consent_updates=consent_updates,
            trigger_source=trigger_source
        )
        logger.info(f"PCI consent updated successfully for contributor {contributor.id}")
        return consent_response
    except HTTPException as e:
        logger.warning(f"PCI consent update failed for contributor {contributor.id}: {e.detail}")
        raise e
    except Exception as e:
        logger.error(f"Unexpected error in PCI consent update for contributor {contributor.id}: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="An unexpected error occurred while updating consent")

@router.get("/consent", response_model=PCIConsentResponse)
async def get_pci_consent_status(
    db: Session = Depends(get_db),
    contributor = Depends(get_current_contributor)
):
    try:
        pci_service = PCIService(db)
        return pci_service.get_consent_status(contributor.id)
    except HTTPException as e:
        if e.status_code == status.HTTP_404_NOT_FOUND:
            return {
                "message": "No PCI consent record found",
                "pci_participation": False,
                "next_steps": "Visit the PCI introduction to learn about voluntary participation"
            }
        raise e
    except Exception as e:
        logger.error(f"Unexpected error retrieving PCI consent for contributor {contributor.id}: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="An unexpected error occurred while retrieving consent status")

# ===== PROFILE MANAGEMENT ENDPOINTS =====

@router.get("/profile", response_model=Optional[TestPersonaProfileResponse])
async def get_test_persona_profile(
    db: Session = Depends(get_db),
    contributor = Depends(get_current_contributor)
):
    try:
        pci_service = PCIService(db)
        return pci_service.get_profile(contributor.id)
    except HTTPException as e:
        raise e
    except Exception as e:
        logger.error(f"Unexpected error retrieving profile for contributor {contributor.id}: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="An unexpected error occurred while retrieving profile")

@router.post("/profile/symbolic-response", response_model=Dict[str, Any])
async def add_symbolic_response(
    response_data: SymbolicResponseCreate,
    db: Session = Depends(get_db),
    contributor = Depends(get_current_contributor)
):
    try:
        pci_service = PCIService(db)
        logger.info(f"Adding symbolic response for contributor {contributor.id}, question: {response_data.question_id}")
        result = pci_service.add_symbolic_response(contributor.id, response_data)
        logger.info(f"Symbolic response added successfully for contributor {contributor.id}")
        return result
    except HTTPException as e:
        logger.warning(f"Symbolic response addition failed for contributor {contributor.id}: {e.detail}")
        raise e
    except Exception as e:
        logger.error(f"Unexpected error adding symbolic response for contributor {contributor.id}: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="An unexpected error occurred while adding symbolic response")

@router.post("/profile/value-priority", response_model=Dict[str, Any])
async def add_value_priority(
    priority_data: ValuePriorityCreate,
    db: Session = Depends(get_db),
    contributor = Depends(get_current_contributor)
):
    try:
        pci_service = PCIService(db)
        logger.info(f"Adding value priority for contributor {contributor.id}, value: {priority_data.value_category}")
        result = pci_service.add_value_priority(contributor.id, priority_data)
        logger.info(f"Value priority added successfully for contributor {contributor.id}")
        return result
    except HTTPException as e:
        logger.warning(f"Value priority addition failed for contributor {contributor.id}: {e.detail}")
        raise e
    except Exception as e:
        logger.error(f"Unexpected error adding value priority for contributor {contributor.id}: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="An unexpected error occurred while adding value priority")

@router.post("/profile/narrative-share", response_model=Dict[str, Any])
async def add_narrative_share(
    narrative_data: NarrativeShareCreate,
    db: Session = Depends(get_db),
    contributor = Depends(get_current_contributor)
):
    try:
        pci_service = PCIService(db)
        logger.info(f"Adding narrative share for contributor {contributor.id}, type: {narrative_data.narrative_type}")
        result = pci_service.add_narrative_share(contributor.id, narrative_data)
        logger.info(f"Narrative share added successfully for contributor {contributor.id}")
        return result
    except HTTPException as e:
        logger.warning(f"Narrative share addition failed for contributor {contributor.id}: {e.detail}")
        raise e
    except Exception as e:
        logger.error(f"Unexpected error adding narrative share for contributor {contributor.id}: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="An unexpected error occurred while adding narrative share")

@router.post("/profile/preference-tag", response_model=Dict[str, Any])
async def add_preference_tag(
    preference_data: PreferenceTagCreate,
    db: Session = Depends(get_db),
    contributor = Depends(get_current_contributor)
):
    try:
        pci_service = PCIService(db)
        logger.info(f"Adding preference tag for contributor {contributor.id}, stimulus: {preference_data.stimulus_type}")
        result = pci_service.add_preference_tag(contributor.id, preference_data)
        logger.info(f"Preference tag added successfully for contributor {contributor.id}")
        return result
    except HTTPException as e:
        logger.warning(f"Preference tag addition failed for contributor {contributor.id}: {e.detail}")
        raise e
    except Exception as e:
        logger.error(f"Unexpected error adding preference tag for contributor {contributor.id}: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="An unexpected error occurred while adding preference tag")

# ...additional endpoints for usage log, feedback, dashboard, admin log-usage, etc. can be added following the same pattern...
