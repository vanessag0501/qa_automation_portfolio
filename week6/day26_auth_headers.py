import requests
import pytest

BASE_URL = "https://httpbin.org"

#-- Part 1: Sending auth headers --

def test_bearer_token_header():
    headers = {
        "Authorization": "Bearer my-test",
        "Content-Type": "application/json"
    }

    response = requests.get(f"{BASE_URL}/headers", headers=headers)
    assert response.status_code == 200

    #httpbin echoes back the headers so we can verify they arrived
    received_headers  = response.json()['headers']
    assert "Authorization" in received_headers
    assert "Bearer my-test" == received_headers["Authorization"]
    print(f"\n  Auth header received: {received_headers['Authorization']}")

#-- Part 2: requests.session -- reuse headers across multiple requests --

def test_session_with_auth_headers():
    session = requests.Session()
    session.headers.update({
        "Authorization" : "Bearer my-session-token",
        "Accept" : "application/json"
    })

    #Every request through this session sends those headers automatically
    response1 = requests.get(f"{BASE_URL}/headers", headers=session.headers)
    response2 = requests.get(f"{BASE_URL}/headers", headers=session.headers)

    assert response1.status_code == 200
    assert response2.status_code == 200 
    
    for response in [response1, response2]:
        headers = response.json()['headers']
        assert "Authorization" in headers
    print(f"  Both requests sent auth header successfully")


#-- Part 3: Basic Auth --
def test_basic_auth():
    # httpbin has a built-in basic auth endpoint
    response = requests.get(
        f"{BASE_URL}/basic-auth/vanessa/password123",
        auth=("vanessa", "password123")
    )
    assert response.status_code == 200
    data = response.json()
    assert data["authenticated"] == True
    assert data["user"] == "vanessa"
    print(f"\n  Basic auth passed for user: {data['user']}")

# -- Part 4: Failed auth --
def test_wrong_credentials():
    response = requests.get(
        f"{BASE_URL}/basic-auth/vanessa/password123",
        auth=("vanessa", "wrongpassword")
    )
    assert response.status_code == 401, \
        f"Expected 401, got {response.status_code}"
    print(f"\n  Wrong credentials correctly returned 401")




