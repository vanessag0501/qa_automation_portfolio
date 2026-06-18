# week6/test_suite.py
import requests
import pytest
import csv

# ── Auth tests ────────────────────────────────────────────────────────
@pytest.mark.regression
def test_bearer_auth(http_url, auth_headers):
    response = requests.get(f"{http_url}/headers", headers=auth_headers)
    assert response.status_code == 200
    received = response.json()["headers"]
    assert "Authorization" in received

def test_basic_auth_pass(http_url):
    response = requests.get(
        f"{http_url}/basic-auth/vanessa/password123",
        auth=("vanessa", "password123")
    )
    assert response.status_code == 200
    assert response.json()["authenticated"] == True

def test_basic_auth_fail(http_url):
    response = requests.get(
        f"{http_url}/basic-auth/vanessa/password123",
        auth=("vanessa", "wrongpassword")
    )
    assert response.status_code == 401

# ── CRUD tests ────────────────────────────────────────────────────────
@pytest.mark.smoke
def test_get_post(api_base_url):
    response = requests.get(f"{api_base_url}/posts/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1

@pytest.mark.smoke
def test_create_post(api_base_url, post_payload):
    response = requests.post(f"{api_base_url}/posts", json=post_payload)
    assert response.status_code == 201
    assert response.json()["title"] == post_payload["title"]

def test_update_post(api_base_url):
    response = requests.put(
        f"{api_base_url}/posts/1",
        json={"title": "Updated", "body": "Updated body", "userId": 1}
    )
    assert response.status_code == 200
    assert response.json()["title"] == "Updated"

def test_delete_post(api_base_url):
    response = requests.delete(f"{api_base_url}/posts/1")
    assert response.status_code == 200

@pytest.mark.smoke
def test_not_found(api_base_url):
    response = requests.get(f"{api_base_url}/posts/9999")
    assert response.status_code == 404

# ── Schema validation ─────────────────────────────────────────────────
def validate_post(post):
    for field, ftype in {"id": int, "userId": int, "title": str, "body": str}.items():
        assert field in post
        assert isinstance(post[field], ftype)

def test_schema_validation(api_base_url):
    response = requests.get(f"{api_base_url}/posts/1")
    validate_post(response.json())

# ── Parametrized tests ────────────────────────────────────────────────
@pytest.mark.parametrize("post_id", [1, 5, 10, 50, 100])
def test_multiple_posts(api_base_url, post_id):
    response = requests.get(f"{api_base_url}/posts/{post_id}")
    assert response.status_code == 200
    assert response.json()["id"] == post_id

# ── Chained test ──────────────────────────────────────────────────────
def test_user_posts_chain(api_base_url):
    user = requests.get(f"{api_base_url}/users/1").json()
    posts = requests.get(
        f"{api_base_url}/posts",
        params={"userId": user["id"]}
    ).json()
    assert len(posts) > 0
    comments = requests.get(
        f"{api_base_url}/posts/{posts[0]['id']}/comments"
    ).json()
    assert len(comments) > 0
    for c in comments:
        assert "email" in c

@pytest.mark.parametrize("post_id,expected_status", [
    (1, 200),
    (50, 200),
    (100, 200),
    (9999, 404)
], ids=["first-post", "mid-post", "last-post", "invalid-post"])
def test_get_post_status(api_client, api_base_url, post_id, expected_status):
    response = api_client.get(f"{api_base_url}/posts/{post_id}")
    assert response.status_code == expected_status, f"Expected status code {expected_status} but got {response.status_code} for post ID {post_id}"