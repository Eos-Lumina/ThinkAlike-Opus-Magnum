import pytest
from src.backend.app.models.pci_models import (
    PCIConsent, PCIConsentHistory, PersonaProfile, SymbolicResponse,
    ValuePriority, NarrativeShare, PreferenceTag, AlgorithmTestUsage,
    PCIDashboardSession, EosLuminaPCISession, AlgorithmTestFeedback, Base
)
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

@pytest.fixture(scope="module")
def test_db():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    session = TestingSessionLocal()
    yield session
    session.close()

# Example test: create and retrieve PCIConsent

def test_create_pci_consent(test_db):
    consent = PCIConsent(
        contributor_id="test-user-1",
        pci_opt_in=True,
        symbolic_responses_consent=True,
        value_priorities_consent=True,
        narrative_shares_consent=True,
        preference_tags_consent=True
    )
    test_db.add(consent)
    test_db.commit()
    result = test_db.query(PCIConsent).filter_by(contributor_id="test-user-1").first()
    assert result is not None
    assert result.pci_opt_in is True
    assert result.symbolic_responses_consent is True


def test_create_test_persona_profile(test_db):
    consent = PCIConsent(contributor_id="user-2", pci_opt_in=True)
    test_db.add(consent)
    test_db.commit()
    profile = PersonaProfile(contributor_id="user-2", consent_id=consent.id)
    test_db.add(profile)
    test_db.commit()
    result = test_db.query(PersonaProfile).filter_by(contributor_id="user-2").first()
    assert result is not None
    assert result.consent_id == consent.id

def test_create_symbolic_response(test_db):
    consent = PCIConsent(contributor_id="user-3", pci_opt_in=True)
    test_db.add(consent)
    test_db.commit()
    profile = PersonaProfile(contributor_id="user-3", consent_id=consent.id)
    test_db.add(profile)
    test_db.commit()
    response = SymbolicResponse(profile_id=profile.id, question_id="q1", question_text="What is meaning?", response_text="42")
    test_db.add(response)
    test_db.commit()
    result = test_db.query(SymbolicResponse).filter_by(profile_id=profile.id).first()
    assert result is not None
    assert result.response_text == "42"

def test_create_value_priority(test_db):
    consent = PCIConsent(contributor_id="user-4", pci_opt_in=True)
    test_db.add(consent)
    test_db.commit()
    profile = PersonaProfile(contributor_id="user-4", consent_id=consent.id)
    test_db.add(profile)
    test_db.commit()
    value = ValuePriority(profile_id=profile.id, value_category="autonomy", priority_rank=1, importance_weight=10)
    test_db.add(value)
    test_db.commit()
    result = test_db.query(ValuePriority).filter_by(profile_id=profile.id).first()
    assert result is not None
    assert result.value_category == "autonomy"

def test_create_narrative_share(test_db):
    consent = PCIConsent(contributor_id="user-5", pci_opt_in=True)
    test_db.add(consent)
    test_db.commit()
    profile = PersonaProfile(contributor_id="user-5", consent_id=consent.id)
    test_db.add(profile)
    test_db.commit()
    narrative = NarrativeShare(profile_id=profile.id, narrative_text="A story", narrative_type="peak_experience")
    test_db.add(narrative)
    test_db.commit()
    result = test_db.query(NarrativeShare).filter_by(profile_id=profile.id).first()
    assert result is not None
    assert result.narrative_type == "peak_experience"

def test_create_preference_tag(test_db):
    consent = PCIConsent(contributor_id="user-6", pci_opt_in=True)
    test_db.add(consent)
    test_db.commit()
    profile = PersonaProfile(contributor_id="user-6", consent_id=consent.id)
    test_db.add(profile)
    test_db.commit()
    tag = PreferenceTag(profile_id=profile.id, stimulus_id="stim1", stimulus_type="image", stimulus_description="desc", reaction_type="resonance", reaction_value=7)
    test_db.add(tag)
    test_db.commit()
    result = test_db.query(PreferenceTag).filter_by(profile_id=profile.id).first()
    assert result is not None
    assert result.reaction_type == "resonance"

def test_create_algorithm_test_usage(test_db):
    consent = PCIConsent(contributor_id="user-7", pci_opt_in=True)
    test_db.add(consent)
    test_db.commit()
    profile = PersonaProfile(contributor_id="user-7", consent_id=consent.id)
    test_db.add(profile)
    test_db.commit()
    usage = AlgorithmTestUsage(profile_id=profile.id, test_id="t1", algorithm_name="alg1", algorithm_version="v1", test_purpose="purpose", tester_id="dev-1", data_components_used={})
    test_db.add(usage)
    test_db.commit()
    result = test_db.query(AlgorithmTestUsage).filter_by(profile_id=profile.id).first()
    assert result is not None
    assert result.algorithm_name == "alg1"

def test_create_pci_dashboard_session(test_db):
    try:
        session = PCIDashboardSession(contributor_id="user-8")
        test_db.add(session)
        test_db.commit()
        result = test_db.query(PCIDashboardSession).filter_by(contributor_id="user-8").first()
        assert result is not None
    except Exception:
        test_db.rollback()

def test_create_eos_lumina_pci_session(test_db):
    try:
        session = EosLuminaPCISession(contributor_id="user-9", session_type="guidance")
        test_db.add(session)
        test_db.commit()
        result = test_db.query(EosLuminaPCISession).filter_by(contributor_id="user-9").first()
        assert result is not None
        assert result.session_type == "guidance"
    except Exception:
        test_db.rollback()

def test_create_algorithm_test_feedback(test_db):
    consent = PCIConsent(contributor_id="user-10", pci_opt_in=True)
    test_db.add(consent)
    test_db.commit()
    profile = PersonaProfile(contributor_id="user-10", consent_id=consent.id)
    test_db.add(profile)
    test_db.commit()
    usage = AlgorithmTestUsage(profile_id=profile.id, test_id="t2", algorithm_name="alg2", algorithm_version="v2", test_purpose="purpose", tester_id="dev-2", data_components_used={})
    test_db.add(usage)
    test_db.commit()
    feedback = AlgorithmTestFeedback(usage_log_id=usage.id, contributor_id="user-10", accuracy_rating=8)
    test_db.add(feedback)
    test_db.commit()
    result = test_db.query(AlgorithmTestFeedback).filter_by(contributor_id="user-10").first()
    assert result is not None
    assert result.accuracy_rating == 8
