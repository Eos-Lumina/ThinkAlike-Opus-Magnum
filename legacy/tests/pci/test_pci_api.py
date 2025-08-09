import pytest
from fastapi.testclient import TestClient
from src.backend.app.main import app

client = TestClient(app)

def test_get_consent_not_found():
    response = client.get("/pci/consent/nonexistent-user")
    assert response.status_code == 404
    assert response.json()["detail"] == "Consent not found"

def test_get_profile_not_found():
    response = client.get("/pci/profile/nonexistent-user")
    assert response.status_code == 404
    assert response.json()["detail"] == "Profile not found"

# Add more tests for valid data when DB/session setup is ready
