# week6/test_suite.py

import requests
import pytest
import csv

# ── Auth tests ────────────────────────────────────────────────────────
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
def test_get_post(base_url):
    response = requests.get(f"{base_url}/posts/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1


def test_create_post(base_url, post_payload):
    response = requests.post(f"{base_url}/posts", json=post_payload)
    assert response.status_code == 201
    assert response.json()["title"] == post_payload["title"]


def test_update_post(base_url):
    response = requests.put(
        f"{base_url}/posts/1",
        json={"title": "Updated", "body": "Updated body", "userId": 1}
    )
    assert response.status_code == 200
    assert response.json()["title"] == "Updated"


def test_delete_post(base_url):
    response = requests.delete(f"{base_url}/posts/1")
    assert response.status_code == 200


def test_not_found(base_url):
    response = requests.get(f"{base_url}/posts/9999")
    assert response.status_code == 404


# ── Schema validation ─────────────────────────────────────────────────
def validate_post(post):
    for field, ftype in {"id": int, "userId": int, "title": str, "body": str}.items():
        assert field in post
        assert isinstance(post[field], ftype)


def test_schema_validation(base_url):
    response = requests.get(f"{base_url}/posts/1")
    validate_post(response.json())


# ── Parametrized tests ────────────────────────────────────────────────
@pytest.mark.parametrize("post_id", [1, 5, 10, 50, 100])
def test_multiple_posts(base_url, post_id):
    response = requests.get(f"{base_urll}/posts/{post_id}")
    assert response.status_code == 200
    assert response.json()["id"] == post_id


# ── Chained test ──────────────────────────────────────────────────────
def test_user_posts_chain(base_url):
    user = requests.get(f"{base_urll}/users/1").json()
    posts = requests.get(
        f"{base_url}/posts",
        params={"userId": user["id"]}
    ).json()
    assert len(posts) > 0

    comments = requests.get(
        f"{base_url}/posts/{posts[0]['id']}/comments"
    ).json()
    assert len(comments) > 0
    for c in comments:
        assert "email" in c