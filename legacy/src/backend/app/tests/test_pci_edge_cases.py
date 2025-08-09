import pytest
from fastapi.testclient import TestClient
from src.backend.app.main import app

client = TestClient(app)

# PersonaProfile edge cases
def test_create_profile_missing_fields():
    # Missing required fields: consent_id, profile_version, symbolic_responses_count, value_priorities_count, narrative_shares_count, preference_tags_count, eos_lumina_guidance_level, profile_depth
    response = client.post("/pci/profile", json={"contributor_id": "test"})
    assert response.status_code == 422

def test_update_profile_not_found():
    # Send all required fields for update
    payload = {
        "contributor_id": "nonexistent",
        "consent_id": "none",
        "profile_version": 1,
        "symbolic_responses_count": 0,
        "value_priorities_count": 0,
        "narrative_shares_count": 0,
        "preference_tags_count": 0,
        "eos_lumina_guidance_level": "standard",
        "profile_depth": "basic"
    }
    response = client.put("/pci/profile/nonexistent", json=payload)
    assert response.status_code == 404

def test_delete_profile_not_found():
    response = client.delete("/pci/profile/nonexistent")
    assert response.status_code == 404

# PCIConsent edge cases
def test_create_consent_missing_fields():
    # Missing required fields: pci_opt_in, symbolic_responses_consent, value_priorities_consent, narrative_shares_consent, preference_tags_consent, consent_version
    response = client.post("/pci/consent", json={"contributor_id": "test"})
    assert response.status_code == 422

def test_update_consent_not_found():
    payload = {
        "contributor_id": "nonexistent",
        "pci_opt_in": True,
        "symbolic_responses_consent": True,
        "value_priorities_consent": True,
        "narrative_shares_consent": True,
        "preference_tags_consent": True,
        "consent_version": "1.0"
    }
    response = client.put("/pci/consent/nonexistent", json=payload)
    assert response.status_code == 404

def test_delete_consent_not_found():
    response = client.delete("/pci/consent/nonexistent")
    assert response.status_code == 404
