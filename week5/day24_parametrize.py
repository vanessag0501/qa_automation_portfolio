import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

#--Basic Parameterization Example-- Same test, multiple inputs
@pytest.mark.parametrize("post_id", [1,2,3,4,5])
def test_get_post_by_id(post_id):
    response = requests.get(f"{BASE_URL}/posts/{post_id}")
    data = response.json()

    assert response.status_code == 200
    assert data['id'] == post_id
    assert "title" in data
    assert "body" in data

#--Parametrize with multiple parameters--
@pytest.mark.parametrize("user_id, expected_count", [
    (1, 10), #userId 1 has 10 posts
    (2, 10), #userId 2 has 10 posts
    (3, 10), #userId 3 has 10 posts
])

def test_filter_posts_by_user(user_id, expected_count):
    response = requests.get(f"{BASE_URL}/posts", params={"userId": user_id})
    posts = response.json()

    assert response.status_code == 200
    assert len(posts) == expected_count, \
        f"User {user_id} expected {expected_count} posts, got {len(posts)}"
    for post in posts:
        assert post["userId"] == user_id

#-- Parametrize for invalid IDs--
@pytest.mark.parametrize("invalid_id", [9999, 0, 99999])
def test_invalid_post_ids(invalid_id):
    response = requests.get(f"{BASE_URL}/posts/{invalid_id}")
    assert response.status_code == 404, \
        f"Expected 404 for post ID {invalid_id}, got {response.status_code}"

#--Parametrize POST payloads--
@pytest.mark.parametrize("title, user_id", [
    ("Test Post 1", 1),
    ("Test Post 2", 2),
    ("Test Post 3", 3),
])
def test_create_post(title, user_id):
    payload = {
        "title": title,
        "body" : "This is a test post created by pytest",
        "userId": user_id
    }

    response = requests.post(f"{BASE_URL}/posts", json=payload)
    created = response.json()

    assert response.status_code == 201
    assert created['title'] == title
    assert created['userId'] == user_id
    assert 'id' in created