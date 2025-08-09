# Persona Calibration Initiative - Database Models
"""
PCI Database Models

This module defines the database models for the Persona Calibration Initiative (PCI),
a voluntary system where contributors can create detailed Test Persona Profiles
to help test and refine ThinkAlike's algorithms.

Core Principles:
- User Sovereignty: Absolute control over participation and data
- Radical Transparency: UI as validation for all processes
- Ethical AI: Eos Lumina as steward, not data harvester
- Purpose Limitation: PCI data firewalled for testing only
- Voluntary Participation: Strictly opt-in system
"""

from sqlalchemy import Column, String, Boolean, DateTime, Text, JSON, ForeignKey, Integer
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from typing import Dict, List, Optional
import uuid

Base = declarative_base()

class PCIConsent(Base):
    """
    Tracks contributor consent for Persona Calibration Initiative participation.
    
    This model ensures granular consent tracking with full audit trail,
    supporting the core principle of User Sovereignty.
    """
    __tablename__ = 'pci_consent'
    
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    contributor_id = Column(String(36), nullable=False, unique=True)  # Pseudonymized ID
    pci_opt_in = Column(Boolean, default=False, nullable=False)
    consent_timestamp = Column(DateTime(timezone=True), server_default=func.now())
    last_updated = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    
    # Granular permissions for different data types
    symbolic_responses_consent = Column(Boolean, default=False)
    value_priorities_consent = Column(Boolean, default=False)
    narrative_shares_consent = Column(Boolean, default=False)
    preference_tags_consent = Column(Boolean, default=False)
    
    # Consent metadata for transparency
    consent_version = Column(String(10), default="1.0")  # Track consent form version
    eos_lumina_session_id = Column(String(36), nullable=True)  # Link to dialogue session
    withdrawal_reason = Column(Text, nullable=True)  # If consent withdrawn
    
    # Relationships
    profile = relationship("PersonaProfile", back_populates="consent", uselist=False)
    consent_history = relationship("PCIConsentHistory", back_populates="consent")

class PCIConsentHistory(Base):
    """
    Audit trail for all consent changes to ensure radical transparency.
    """
    __tablename__ = 'pci_consent_history'
    
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    consent_id = Column(String(36), ForeignKey('pci_consent.id'), nullable=False)
    action = Column(String(50), nullable=False)  # 'opt_in', 'opt_out', 'permission_update'
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    previous_state = Column(JSON, nullable=True)
    new_state = Column(JSON, nullable=False)
    trigger_source = Column(String(100), nullable=True)  # 'eos_lumina_dialogue', 'user_dashboard', etc.
    
    # Relationships
    consent = relationship("PCIConsent", back_populates="consent_history")

class PersonaProfile(Base):
    """
    Core Test Persona Profile for algorithm calibration.
    
    Contains all voluntary data shared by contributors for algorithm testing,
    with strict purpose limitation and sovereignty controls.
    """
    __tablename__ = 'persona_profiles'
    
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    contributor_id = Column(String(36), nullable=False, unique=True)  # Pseudonymized ID
    consent_id = Column(String(36), ForeignKey('pci_consent.id'), nullable=False)
    
    profile_creation_date = Column(DateTime(timezone=True), server_default=func.now())
    profile_last_modified = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    profile_version = Column(Integer, default=1)  # For versioning profile updates
    
    # Profile completeness indicators
    symbolic_responses_count = Column(Integer, default=0)
    value_priorities_count = Column(Integer, default=0)
    narrative_shares_count = Column(Integer, default=0)
    preference_tags_count = Column(Integer, default=0)
    
    # Metadata
    eos_lumina_guidance_level = Column(String(20), default="standard")  # 'minimal', 'standard', 'oracle'
    profile_depth = Column(String(20), default="basic")  # 'basic', 'detailed', 'comprehensive'
    
    # Relationships
    consent = relationship("PCIConsent", back_populates="profile")
    symbolic_responses = relationship("SymbolicResponse", back_populates="profile")
    value_priorities = relationship("ValuePriority", back_populates="profile")
    narrative_shares = relationship("NarrativeShare", back_populates="profile")
    preference_tags = relationship("PreferenceTag", back_populates="profile")
    usage_log = relationship("AlgorithmTestUsage", back_populates="profile")

class SymbolicResponse(Base):
    """
    Responses to symbolic questions from the Portal Realm question pool.
    
    These responses help calibrate algorithms for meaning-making and symbolic understanding.
    """
    __tablename__ = 'symbolic_responses'
    
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    profile_id = Column(String(36), ForeignKey('persona_profiles.id'), nullable=False)
    
    question_id = Column(String(36), nullable=False)  # Reference to symbolic question
    question_text = Column(Text, nullable=False)  # Stored for audit trail
    response_text = Column(Text, nullable=False)
    response_timestamp = Column(DateTime(timezone=True), server_default=func.now())
    
    # Response metadata
    response_depth = Column(String(20), default="standard")  # 'brief', 'standard', 'detailed'
    emotional_resonance = Column(Integer, nullable=True)  # 1-10 self-reported resonance
    symbolic_archetype = Column(String(50), nullable=True)  # Auto-detected or user-selected
    
    # Eos Lumina interaction context
    eos_lumina_follow_up = Column(Text, nullable=True)
    eos_lumina_insight = Column(Text, nullable=True)
    
    # Relationships
    profile = relationship("PersonaProfile", back_populates="symbolic_responses")

class ValuePriority(Base):
    """
    Value prioritization data from interactive value exploration.
    
    Helps calibrate algorithms for value-based matching and personalization.
    """
    __tablename__ = 'value_priorities'
    
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    profile_id = Column(String(36), ForeignKey('persona_profiles.id'), nullable=False)
    
    value_category = Column(String(100), nullable=False)  # e.g., "autonomy", "connection", "growth"
    priority_rank = Column(Integer, nullable=False)  # 1-N ranking
    importance_weight = Column(Integer, nullable=False)  # 1-10 importance scale
    
    # Custom explanations
    personal_definition = Column(Text, nullable=True)
    priority_reasoning = Column(Text, nullable=True)
    life_example = Column(Text, nullable=True)
    
    # Context metadata
    exploration_session_id = Column(String(36), nullable=True)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationships
    profile = relationship("PersonaProfile", back_populates="value_priorities")

class NarrativeShare(Base):
    """
    Secure narrative capture with sensitivity controls.
    
    Contains personal stories and experiences that contributors choose to share
    for algorithm understanding of human narrative patterns.
    """
    __tablename__ = 'narrative_shares'
    
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    profile_id = Column(String(36), ForeignKey('persona_profiles.id'), nullable=False)
    
    narrative_title = Column(String(200), nullable=True)
    narrative_text = Column(Text, nullable=False)
    narrative_type = Column(String(50), nullable=False)  # 'peak_experience', 'transformation', 'value_story'
    
    # Sensitivity and anonymization controls
    sensitivity_level = Column(String(20), default="standard")  # 'low', 'standard', 'high', 'very_high'
    anonymization_preference = Column(String(20), default="partial")  # 'none', 'partial', 'full'
    algorithm_use_consent = Column(Boolean, default=True)
    
    # Content metadata
    emotional_tone = Column(String(50), nullable=True)
    life_stage = Column(String(50), nullable=True)
    core_themes = Column(JSON, nullable=True)  # List of identified themes
    
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationships
    profile = relationship("PersonaProfile", back_populates="narrative_shares")

class PreferenceTag(Base):
    """
    Preference tagging from diverse stimuli presentation.
    
    Captures reactions to various content, experiences, and stimuli
    to help calibrate recommendation and personalization algorithms.
    """
    __tablename__ = 'preference_tags'
    
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    profile_id = Column(String(36), ForeignKey('persona_profiles.id'), nullable=False)
    
    stimulus_id = Column(String(36), nullable=False)
    stimulus_type = Column(String(50), nullable=False)  # 'image', 'text', 'concept', 'scenario'
    stimulus_description = Column(Text, nullable=False)
    
    # Reaction data
    reaction_type = Column(String(50), nullable=False)  # 'resonance', 'preference', 'emotional_response'
    reaction_value = Column(Integer, nullable=False)  # Numeric scale (e.g., 1-10)
    reaction_explanation = Column(Text, nullable=True)
    
    # Context metadata
    presentation_context = Column(String(100), nullable=True)
    response_time_ms = Column(Integer, nullable=True)
    confidence_level = Column(Integer, nullable=True)  # 1-10
    
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationships
    profile = relationship("PersonaProfile", back_populates="preference_tags")

class AlgorithmTestUsage(Base):
    """
    Audit trail for all algorithm tests using contributor profiles.
    
    Ensures radical transparency by tracking exactly how contributor data
    is used in algorithm testing and refinement.
    """
    __tablename__ = 'algorithm_test_usage'
    
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    profile_id = Column(String(36), ForeignKey('persona_profiles.id'), nullable=False)
    
    test_id = Column(String(36), nullable=False)
    algorithm_name = Column(String(100), nullable=False)
    algorithm_version = Column(String(20), nullable=False)
    test_purpose = Column(Text, nullable=False)
    
    # Test execution details
    test_timestamp = Column(DateTime(timezone=True), server_default=func.now())
    tester_id = Column(String(36), nullable=False)  # Developer/researcher ID
    test_parameters = Column(JSON, nullable=True)
    
    # Data usage specifics
    data_components_used = Column(JSON, nullable=False)  # Which profile components were used
    processing_duration_ms = Column(Integer, nullable=True)
    
    # Results (anonymized for contributor transparency)
    test_results_summary = Column(JSON, nullable=True)
    accuracy_metrics = Column(JSON, nullable=True)
    contributor_feedback_requested = Column(Boolean, default=False)
    
    # Relationships
    profile = relationship("PersonaProfile", back_populates="usage_log")

class PCIDashboardSession(Base):
    """
    Tracks contributor dashboard sessions for transparency and support.
    """
    __tablename__ = 'pci_dashboard_sessions'
    
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    contributor_id = Column(String(36), nullable=False)
    
    session_start = Column(DateTime(timezone=True), server_default=func.now())
    session_end = Column(DateTime(timezone=True), nullable=True)
    
    # Session activity tracking
    pages_viewed = Column(JSON, nullable=True)  # List of dashboard pages accessed
    actions_taken = Column(JSON, nullable=True)  # List of actions performed
    eos_lumina_interactions = Column(Integer, default=0)
    
    # Support indicators
    help_requests = Column(Integer, default=0)
    confusion_indicators = Column(JSON, nullable=True)
    satisfaction_rating = Column(Integer, nullable=True)  # End-of-session rating

# Additional supporting models for enhanced functionality

class EosLuminaPCISession(Base):
    """
    Tracks Eos Lumina dialogue sessions related to PCI guidance.
    """
    __tablename__ = 'eos_lumina_pci_sessions'
    
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    contributor_id = Column(String(36), nullable=False)
    session_type = Column(String(50), nullable=False)  # 'introduction', 'consent', 'guidance', 'oracle'
    
    session_start = Column(DateTime(timezone=True), server_default=func.now())
    session_end = Column(DateTime(timezone=True), nullable=True)
    
    # Dialogue tracking
    dialogue_turns = Column(Integer, default=0)
    topics_covered = Column(JSON, nullable=True)
    guidance_level = Column(String(20), default="standard")
    
    # Outcomes
    consent_decision = Column(String(20), nullable=True)  # 'opted_in', 'declined', 'deferred'
    profile_actions_taken = Column(JSON, nullable=True)
    satisfaction_indicators = Column(JSON, nullable=True)

class AlgorithmTestFeedback(Base):
    """
    Structured feedback from contributors on algorithm test results.
    """
    __tablename__ = 'algorithm_test_feedback'
    
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    usage_log_id = Column(String(36), ForeignKey('algorithm_test_usage.id'), nullable=False)
    contributor_id = Column(String(36), nullable=False)
    
    # Feedback content
    accuracy_rating = Column(Integer, nullable=True)  # 1-10
    relevance_rating = Column(Integer, nullable=True)  # 1-10
    surprise_factor = Column(Integer, nullable=True)  # 1-10
    
    qualitative_feedback = Column(Text, nullable=True)
    improvement_suggestions = Column(Text, nullable=True)
    
    # Feedback metadata
    feedback_timestamp = Column(DateTime(timezone=True), server_default=func.now())
    feedback_confidence = Column(Integer, nullable=True)  # 1-10
    would_test_again = Column(Boolean, nullable=True)
    
    # Relationships
    usage_log = relationship("AlgorithmTestUsage")
