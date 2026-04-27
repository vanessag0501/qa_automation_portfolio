import requests 
import pytest

BASE_URL = "https://jsonplaceholder.typicode.com"

#Chain 1: Create a post, then verify it exists

def test_create_and_verify_post():
    # Step 1: Create a post
    payload ={
        "title" : " Chained test post",
        "body" : " Created in ste 1",
        "userId" : 1
    }

    create_respone = requests.post(f" {BASE_URL}/posts", json=payload)
    assert create_respone.status_code == 201
    created_post = create_respone.json()
    post_id = created_post['id']
    print(f"  Created post with ID {post_id}")

    #Step 2: use the ID from step 1 to fetch the post
    # Note: JSONPlaceholder is a fake API so it won't actually
    # store our post — we verify post 1 exists to simulate the flow

    get_response = requests.get(f"{BASE_URL}/posts/1")
    assert get_response.status_code == 200
    fetched_post = get_response.json()
    assert fetched_post['id'] == 1
    print(f"  Successfully fetched post with ID {fetched_post['id']}")

    #Step 3: Get comments for that post
    comments_response = requests.get(f"{BASE_URL}/posts/1/comments")
    assert comments_response.status_code == 200
    comments = comments_response.json()
    assert len(comments) > 0, "Expected comments for post ID 1"
    print(f"  Retrieved {len(comments)} comments for post ID 1")
    print(" Chain 1 passed")


#-- Chain 2: Gegt a user, then their posts, then get comments--
def test_user_posts_comments_chain():
    # Step 1: Get user info
    user_response = requests.get(f"{BASE_URL}/users/1")
    assert user_response.status_code == 200
    user = user_response.json()
    user_id = user['id']
    print(f"  Fetched user with ID {user_id}")

    # Step 2: Get posts for that user
    posts_response = requests.get(f"{BASE_URL}/posts", params={"userId": user_id})
    assert posts_response.status_code == 200
    posts = posts_response.json()
    assert len(posts) > 0
    first_post_id = posts[0]["id"]
    print(f"  Step 2 — found {len(posts)} posts, first ID is {first_post_id}")

    # Step 3: Get comments for the first post
    comments_response = requests.get(f"{BASE_URL}/posts/{first_post_id}/comments")
    assert comments_response.status_code == 200
    comments = comments_response.json()
    assert len(comments) > 0

    #Step 4 - verify every comment has an email field
    for comments in comments:
        assert "email" in comments, f"Comment ID {comments['id']} is missing email field"
        assert "@" in comments['email'], f"Comment ID {comments['id']} has invalid email: {comments['email']}"

    print(f"  Step 3 — {len(comments)} comments, all have valid emails")

    print("  Chain 2 passed")


#-- Chain 3: Full CRUD Chain --

def test_full_crud_chain():
    # CREATE
    payload = {"title": "CRUD chain test", "body": "Step 1", "userId": 1}
    response = requests.post(f"{BASE_URL}/posts", json=payload)
    assert response.status_code == 201
    post_id = response.json()["id"]
    print(f"\n  CREATE — post ID {post_id}")

    existing_id = 1

    # UPDATE
    updated = {"title": "Updated title", "body": "Step 2", "userId": 1}
    response = requests.put(f"{BASE_URL}/posts/{existing_id}", json=updated)
    assert response.status_code == 200
    assert response.json()["title"] == "Updated title"
    print(f"  UPDATE — title changed successfully")

    # PATCH — partial update
    patch = {"title": "Patched title"}
    response = requests.patch(f"{BASE_URL}/posts/{existing_id}", json=patch)
    assert response.status_code == 200
    assert response.json()["title"] == "Patched title"
    print(f"  PATCH  — partial update successful")

    # DELETE
    response = requests.delete(f"{BASE_URL}/posts/{existing_id}")
    assert response.status_code == 200
    print(f"  DELETE — post removed")

    print("  Chain 3 passed")