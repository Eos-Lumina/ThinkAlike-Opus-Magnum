import requests
import json

BASE_URL = "http://127.0.0.1:8000"

# List of endpoints to test (add more as needed)
endpoints = [
    {"method": "GET", "path": "/"},
    {"method": "GET", "path": "/openapi.json"},
    # Auth endpoints
    {"method": "POST", "path": "/api/v1/auth/register", "json": {"email": "testuser@example.com", "username": "testuser", "password": "testpass"}},
    {"method": "POST", "path": "/api/v1/auth/token", "data": {"username": "testuser", "password": "testpass"}},
    # Users endpoints
    {"method": "GET", "path": "/api/v1/users/1"},
    # Items endpoints (GET all, GET by id)
    {"method": "GET", "path": "/api/v1/items/"},
    {"method": "GET", "path": "/api/v1/items/1"},
    # Profiles endpoints
    {"method": "GET", "path": "/api/v1/profiles/me"},
    # Eos endpoint (system event)
    {"method": "POST", "path": "/api/v1/eos/events/system", "json": {"event_type": "user_speaks", "session_id": "testsession", "user_id": "testuser"}},
]

def test_endpoint(method, path, headers=None, **kwargs):
    url = BASE_URL + path
    try:
        resp = requests.request(method, url, timeout=5, headers=headers, **kwargs)
        print(f"{method} {path} -> {resp.status_code}")
        if resp.status_code >= 400:
            print(f"  ERROR: {resp.text}")
        else:
            try:
                print(f"  Response: {json.dumps(resp.json(), indent=2)}")
            except Exception:
                print(f"  Response: {resp.text}")
        return resp
    except Exception as e:
        print(f"{method} {path} -> EXCEPTION: {e}")
        return None

if __name__ == "__main__":
    token = None
    # Register user
    reg_resp = test_endpoint("POST", "/api/v1/auth/register", json={"email": "testuser@example.com", "username": "testuser", "password": "testpass"})
    # Get token
    token_resp = test_endpoint("POST", "/api/v1/auth/token", data={"username": "testuser", "password": "testpass"})
    if token_resp and token_resp.status_code == 200:
        try:
            token = token_resp.json().get("access_token")
        except Exception:
            token = None
    auth_headers = {"Authorization": f"Bearer {token}"} if token else None

    # Test endpoints with and without auth as appropriate
    test_endpoint("GET", "/", headers=auth_headers)
    test_endpoint("GET", "/openapi.json", headers=auth_headers)
    test_endpoint("GET", "/api/v1/users/1", headers=auth_headers)
    test_endpoint("GET", "/api/v1/items/", headers=auth_headers)
    test_endpoint("GET", "/api/v1/items/1", headers=auth_headers)
    test_endpoint("GET", "/api/v1/profiles/me", headers=auth_headers)
    test_endpoint("POST", "/api/v1/eos/events/system", headers=auth_headers, json={"event_type": "user_speaks", "session_id": "testsession", "user_id": "testuser"})
