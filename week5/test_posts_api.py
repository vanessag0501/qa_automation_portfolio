import requests 

def validate_post_schema(post):
    required_fields = {
        "id": int,
        "userId": int,
        "title": str,
        "body": str
    }
    for field, expected_type in required_fields.items():
        assert field in post, f"Missing field: {field}"
        assert isinstance(post[field], expected_type), \
            f"Field '{field}' should be {expected_type}, got {type(post[field])}"

def test_get_single_post(base_url):
    response = requests.get(f"{base_url}/posts/1")
    assert response.status_code == 200
    assert response.elapsed.total_seconds() < 2, "Response took too long"
    validate_post_schema(response.json())

def test_get_all_posts(base_url):
    response = requests.get(f"{base_url}/posts")
    posts = response.json()
    assert response.status_code == 200
    assert len(posts) == 100
    assert isinstance(posts, list)

def test_filter_posts_by_user(base_url):
    response = requests.get(f"{base_url}/posts", params={"userId": 1})
    filtered = response.json()
    assert response.status_code == 200
    assert len(filtered) > 0, "No posts returned for userId=1"
    for post in filtered:
        assert post['userId'] == 1, f"Expected userId 1, got {post['userId']}"

def test_create_post(base_url, post_payload):
    response = requests.post(f"{base_url}/posts", json=post_payload)
    created  = response.json()
    assert response.status_code == 201
    assert created['title'] == post_payload['title'], "Title mismatch"
    assert 'id' in created, "No ID in response"

def test_update_post(base_url):
    updated_post = {
        "title":  "Updated QA Post",
        "body":   "This post was updated",
        "userId": 1
    }
    response = requests.put(f"{base_url}/posts/1", json=updated_post)
    data  = response.json()
    assert response.status_code == 200
    assert data['title'] == "Updated QA Post", "Title not updated"

def test_delete_post(base_url):
    response = requests.delete(f"{base_url}/posts/1")
    assert response.status_code == 200 

def test_post_not_found(base_url):
    response = requests.get(f"{base_url}/posts/9999")
    assert response.status_code == 404, f"Expected 404, got {response.status_code}"

def test_response_headers(base_url):
    response = requests.get(f"{base_url}/posts/1")
    assert "application/json" in response.headers['Content-Type']