# Persona Calibration Initiative - Database Models
"""
PCI Database Models

This module defines the database models for the Persona Calibration Initiative (PCI),
a voluntary system where contributors can create detailed Persona Profiles
to help test and refine ThinkAlike's algorithms.

Core Principles:
- User Sovereignty: Absolute control over participation and data
- Radical Transparency: UI as validation for all processes
- Ethical AI: Eos Lumina as steward, not data harvester
- Purpose Limitation: PCI data firewalled for testing only
- Voluntary Participation: Strictly opt-in system
"""

from sqlalchemy import Column, String, Boolean, DateTime, Text, JSON, ForeignKey, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import uuid

Base = declarative_base()

class PCIConsent(Base):
    __tablename__ = 'pci_consent'
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    contributor_id = Column(String(36), nullable=False, unique=True)
    pci_opt_in = Column(Boolean, default=False, nullable=False)
    consent_timestamp = Column(DateTime(timezone=True), server_default=func.now())
    last_updated = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    symbolic_responses_consent = Column(Boolean, default=False)
    value_priorities_consent = Column(Boolean, default=False)
    narrative_shares_consent = Column(Boolean, default=False)
    preference_tags_consent = Column(Boolean, default=False)
    consent_version = Column(String(10), default="1.0")
    eos_lumina_session_id = Column(String(36), nullable=True)
    withdrawal_reason = Column(Text, nullable=True)
    profile = relationship("PersonaProfile", back_populates="consent", uselist=False)
    consent_history = relationship("PCIConsentHistory", back_populates="consent")

class PCIConsentHistory(Base):
    __tablename__ = 'pci_consent_history'
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    consent_id = Column(String(36), ForeignKey('pci_consent.id'), nullable=False)
    action = Column(String(50), nullable=False)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    previous_state = Column(JSON, nullable=True)
    new_state = Column(JSON, nullable=False)
    trigger_source = Column(String(100), nullable=True)
    consent = relationship("PCIConsent", back_populates="consent_history")

class PersonaProfile(Base):
    __tablename__ = 'persona_profiles'
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    contributor_id = Column(String(36), nullable=False, unique=True)
    consent_id = Column(String(36), ForeignKey('pci_consent.id'), nullable=False)
    profile_creation_date = Column(DateTime(timezone=True), server_default=func.now())
    profile_last_modified = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    profile_version = Column(Integer, default=1)
    symbolic_responses_count = Column(Integer, default=0)
    value_priorities_count = Column(Integer, default=0)
    narrative_shares_count = Column(Integer, default=0)
    preference_tags_count = Column(Integer, default=0)
    eos_lumina_guidance_level = Column(String(20), default="standard")
    profile_depth = Column(String(20), default="basic")
    consent = relationship("PCIConsent", back_populates="profile")
    symbolic_responses = relationship("SymbolicResponse", back_populates="profile")
    value_priorities = relationship("ValuePriority", back_populates="profile")
    narrative_shares = relationship("NarrativeShare", back_populates="profile")
    preference_tags = relationship("PreferenceTag", back_populates="profile")
    usage_log = relationship("AlgorithmTestUsage", back_populates="profile")

class SymbolicResponse(Base):
    __tablename__ = 'symbolic_responses'
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    profile_id = Column(String(36), ForeignKey('persona_profiles.id'), nullable=False)
    question_id = Column(String(36), nullable=False)
    question_text = Column(Text, nullable=False)
    response_text = Column(Text, nullable=False)
    response_timestamp = Column(DateTime(timezone=True), server_default=func.now())
    response_depth = Column(String(20), default="standard")
    emotional_resonance = Column(Integer, nullable=True)
    symbolic_archetype = Column(String(50), nullable=True)
    eos_lumina_follow_up = Column(Text, nullable=True)
    eos_lumina_insight = Column(Text, nullable=True)
    profile = relationship("PersonaProfile", back_populates="symbolic_responses")

class ValuePriority(Base):
    __tablename__ = 'value_priorities'
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    profile_id = Column(String(36), ForeignKey('persona_profiles.id'), nullable=False)
    value_category = Column(String(100), nullable=False)
    priority_rank = Column(Integer, nullable=False)
    importance_weight = Column(Integer, nullable=False)
    personal_definition = Column(Text, nullable=True)
    priority_reasoning = Column(Text, nullable=True)
    life_example = Column(Text, nullable=True)
    exploration_session_id = Column(String(36), nullable=True)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    profile = relationship("PersonaProfile", back_populates="value_priorities")

class NarrativeShare(Base):
    __tablename__ = 'narrative_shares'
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    profile_id = Column(String(36), ForeignKey('persona_profiles.id'), nullable=False)
    narrative_title = Column(String(200), nullable=True)
    narrative_text = Column(Text, nullable=False)
    narrative_type = Column(String(50), nullable=False)
    sensitivity_level = Column(String(20), default="standard")
    anonymization_preference = Column(String(20), default="partial")
    algorithm_use_consent = Column(Boolean, default=True)
    emotional_tone = Column(String(50), nullable=True)
    life_stage = Column(String(50), nullable=True)
    core_themes = Column(JSON, nullable=True)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    profile = relationship("PersonaProfile", back_populates="narrative_shares")

class PreferenceTag(Base):
    __tablename__ = 'preference_tags'
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    profile_id = Column(String(36), ForeignKey('persona_profiles.id'), nullable=False)
    stimulus_id = Column(String(36), nullable=False)
    stimulus_type = Column(String(50), nullable=False)
    stimulus_description = Column(Text, nullable=False)
    reaction_type = Column(String(50), nullable=False)
    reaction_value = Column(Integer, nullable=False)
    reaction_explanation = Column(Text, nullable=True)
    presentation_context = Column(String(100), nullable=True)
    response_time_ms = Column(Integer, nullable=True)
    confidence_level = Column(Integer, nullable=True)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    profile = relationship("PersonaProfile", back_populates="preference_tags")

class AlgorithmTestUsage(Base):
    __tablename__ = 'algorithm_test_usage'
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    profile_id = Column(String(36), ForeignKey('persona_profiles.id'), nullable=False)
    test_id = Column(String(36), nullable=False)
    algorithm_name = Column(String(100), nullable=False)
    algorithm_version = Column(String(20), nullable=False)
    test_purpose = Column(Text, nullable=False)
    test_timestamp = Column(DateTime(timezone=True), server_default=func.now())
    tester_id = Column(String(36), nullable=False)
    test_parameters = Column(JSON, nullable=True)
    data_components_used = Column(JSON, nullable=False)
    processing_duration_ms = Column(Integer, nullable=True)
    test_results_summary = Column(JSON, nullable=True)
    accuracy_metrics = Column(JSON, nullable=True)
    contributor_feedback_requested = Column(Boolean, default=False)
    profile = relationship("PersonaProfile", back_populates="usage_log")

class PCIDashboardSession(Base):
    __tablename__ = 'pci_dashboard_sessions'
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    contributor_id = Column(String(36), nullable=False)
    session_start = Column(DateTime(timezone=True), server_default=func.now())
    session_end = Column(DateTime(timezone=True), nullable=True)
    pages_viewed = Column(JSON, nullable=True)
    actions_taken = Column(JSON, nullable=True)
    eos_lumina_interactions = Column(Integer, default=0)
    help_requests = Column(Integer, default=0)
    confusion_indicators = Column(JSON, nullable=True)
    satisfaction_rating = Column(Integer, nullable=True)

class EosLuminaPCISession(Base):
    __tablename__ = 'eos_lumina_pci_sessions'
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    contributor_id = Column(String(36), nullable=False)
    session_type = Column(String(50), nullable=False)
    session_start = Column(DateTime(timezone=True), server_default=func.now())
    session_end = Column(DateTime(timezone=True), nullable=True)
    dialogue_turns = Column(Integer, default=0)
    topics_covered = Column(JSON, nullable=True)
    guidance_level = Column(String(20), default="standard")
    consent_decision = Column(String(20), nullable=True)
    profile_actions_taken = Column(JSON, nullable=True)
    satisfaction_indicators = Column(JSON, nullable=True)

class AlgorithmTestFeedback(Base):
    __tablename__ = 'algorithm_test_feedback'
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    usage_log_id = Column(String(36), ForeignKey('algorithm_test_usage.id'), nullable=False)
    contributor_id = Column(String(36), nullable=False)
    accuracy_rating = Column(Integer, nullable=True)
    relevance_rating = Column(Integer, nullable=True)
    surprise_factor = Column(Integer, nullable=True)
    qualitative_feedback = Column(Text, nullable=True)
    improvement_suggestions = Column(Text, nullable=True)
    feedback_timestamp = Column(DateTime(timezone=True), server_default=func.now())
    feedback_confidence = Column(Integer, nullable=True)
    would_test_again = Column(Boolean, nullable=True)
    usage_log = relationship("AlgorithmTestUsage")
