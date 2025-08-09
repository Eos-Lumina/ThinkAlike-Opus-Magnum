from fastapi.testclient import TestClient

def test_register_and_login(client: TestClient):
    # Register a new user
    response = client.post(
        "/api/v1/auth/register",
        json={
            "email": "testuser@example.com",
            "username": "testuser",
            "password": "testpassword123",
            "role": "user",
        },
    )
    assert response.status_code in (200, 201)

    # Login
    response = client.post(
        "/api/v1/auth/token",
        data={"username": "testuser", "password": "testpassword123"},
    )
    assert response.status_code == 200
    token = response.json().get("access_token")
    assert token

    # Access a protected endpoint
    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/api/v1/users/", headers=headers)
    assert response.status_code == 200  # Expect 200 OK now
