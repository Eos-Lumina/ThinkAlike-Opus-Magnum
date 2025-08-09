# Persona Calibration Initiative - Pydantic Schemas
# ...rescued and harmonized from legacy canonical source...

from pydantic import BaseModel, Field, validator, ConfigDict
from typing import Dict, List, Optional, Any
from datetime import datetime
from enum import Enum

class GuidanceLevel(str, Enum):
    MINIMAL = "minimal"
    STANDARD = "standard"
    ORACLE = "oracle"

class ProfileDepth(str, Enum):
    BASIC = "basic"
    DETAILED = "detailed"
    COMPREHENSIVE = "comprehensive"

class SensitivityLevel(str, Enum):
    LOW = "low"
    STANDARD = "standard"
    HIGH = "high"
    VERY_HIGH = "very_high"

class AnonymizationPreference(str, Enum):
    NONE = "none"
    PARTIAL = "partial"
    FULL = "full"

class GranularPermissions(BaseModel):
    symbolic_responses: bool = Field(default=False)
    value_priorities: bool = Field(default=False)
    narrative_shares: bool = Field(default=False)
    preference_tags: bool = Field(default=False)
    model_config = ConfigDict(from_attributes=True)

class GuidancePreferences(BaseModel):
    level: GuidanceLevel = Field(default=GuidanceLevel.STANDARD)
    oracle_access: bool = Field(default=False)
    proactive_support: bool = Field(default=True)
    model_config = ConfigDict(from_attributes=True)

class PCIConsentCreate(BaseModel):
    pci_opt_in: bool = Field(...)
    granular_permissions: GranularPermissions = Field(...)
    guidance_preferences: GuidancePreferences = Field(default_factory=GuidancePreferences)
    model_config = ConfigDict(from_attributes=True)

class PCIConsentUpdate(BaseModel):
    pci_opt_in: Optional[bool] = Field(None)
    granular_permissions: Optional[GranularPermissions] = Field(None)
    guidance_preferences: Optional[GuidancePreferences] = Field(None)
    withdrawal_reason: Optional[str] = Field(None)
    model_config = ConfigDict(from_attributes=True)

class PCIConsentResponse(BaseModel):
    id: str = Field(...)
    contributor_id: str = Field(...)
    pci_opt_in: bool = Field(...)
    consent_timestamp: datetime = Field(...)
    last_updated: datetime = Field(...)
    granular_permissions: Dict[str, bool] = Field(...)
    consent_version: str = Field(...)
    has_profile: bool = Field(...)
    profile_id: Optional[str] = Field(None)
    model_config = ConfigDict(from_attributes=True)

class TestPersonaProfileCreate(BaseModel):
    eos_lumina_guidance_level: GuidanceLevel = Field(default=GuidanceLevel.STANDARD)
    profile_depth: ProfileDepth = Field(default=ProfileDepth.BASIC)
    model_config = ConfigDict(from_attributes=True)

class CompletenessMetrics(BaseModel):
    symbolic_responses_count: int = Field(...)
    value_priorities_count: int = Field(...)
    narrative_shares_count: int = Field(...)
    preference_tags_count: int = Field(...)
    model_config = ConfigDict(from_attributes=True)
    @property
    def total_data_points(self) -> int:
        return (
            self.symbolic_responses_count +
            self.value_priorities_count +
            self.narrative_shares_count +
            self.preference_tags_count
        )

class TestPersonaProfileResponse(BaseModel):
    id: str = Field(...)
    contributor_id: str = Field(...)
    profile_creation_date: datetime = Field(...)
    profile_last_modified: datetime = Field(...)
    profile_version: int = Field(...)
    completeness_metrics: CompletenessMetrics = Field(...)
    eos_lumina_guidance_level: GuidanceLevel = Field(...)
    profile_depth: ProfileDepth = Field(...)
    consent_status: PCIConsentResponse = Field(...)
    model_config = ConfigDict(from_attributes=True)

class SymbolicResponseCreate(BaseModel):
    question_id: str = Field(...)
    question_text: str = Field(...)
    response_text: str = Field(..., min_length=10)
    response_depth: str = Field(default="standard")
    emotional_resonance: Optional[int] = Field(None, ge=1, le=10)
    symbolic_archetype: Optional[str] = Field(None)
    eos_lumina_follow_up: Optional[str] = Field(None)
    eos_lumina_insight: Optional[str] = Field(None)
    @validator('response_text')
    def validate_response_content(cls, v):
        if len(v.strip()) < 10:
            raise ValueError('Response must be at least 10 characters long')
        return v.strip()
    model_config = ConfigDict(from_attributes=True)
# ...additional schemas for ValuePriorityCreate, NarrativeShareCreate, PreferenceTagCreate, etc. should be added here following the same pattern...
