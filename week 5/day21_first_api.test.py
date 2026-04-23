import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

response = requests.get(f"{BASE_URL}/posts/1")

#The three things you should always check in an API response:
print(f"Status code: {response.status_code}") #200 means success
print(f"Response Time: {response.elapsed.total_seconds()} seconds") #how long did it take to get a response?
print(f"Content type: {response.headers['Content-Type']}") #what kind of data is in the response?

# The actual data
data = response.json() #turns the response into a Python dictionary
print(f"\nPost ID: {data['id']}")
print(f"User ID: {data['userId']}")
print(f"Title: {data['title']}")

#-- Assertions --

assert response.status_code == 200, f" Expected 200, got {response.status_code}"
assert data['id'] == 1, "Wrong post ID returned"
assert 'title' in data, "Title is missing from response"
assert 'body' in data, "Body field is missing from response"
assert response.elapsed.total_seconds() < 2, "Response took too slow"

print("\nAll assertions passed!")

# ── GET all posts ─────────────────────────────────────────────────────
response = requests.get(f"{BASE_URL}/posts")
posts = response.json()

assert response.status_code == 200
assert len(posts) == 100, f"Expected 100 posts, got {len(posts)}"
assert isinstance(posts, list), "Expected a list"
print(f"\nGET all posts  : {len(posts)} posts returned")

# ── POST — create a new post ──────────────────────────────────────────
new_post = {
    "title":  "QA Automation Test Post",
    "body":   "Created by Vanessa's API test suite",
    "userId": 1
}

response = requests.post(f"{BASE_URL}/posts", json=new_post)
created  = response.json()

assert response.status_code == 201, f"Expected 201, got {response.status_code}"
assert created['title'] == new_post['title'], "Title mismatch"
assert 'id' in created, "No ID in response"
print(f"POST new post  : created with ID {created['id']}")

# ── PUT — update a post ───────────────────────────────────────────────
updated_post = {
    "title":  "Updated QA Post",
    "body":   "This post was updated",
    "userId": 1
}

response = requests.put(f"{BASE_URL}/posts/1", json=updated_post)
updated  = response.json()

assert response.status_code == 200
assert updated['title'] == "Updated QA Post", "Title not updated"
print(f"PUT update post: title is now '{updated['title']}'")

# ── DELETE — delete a post ────────────────────────────────────────────
response = requests.delete(f"{BASE_URL}/posts/1")

assert response.status_code == 200, f"Expected 200, got {response.status_code}"
print(f"DELETE post    : status {response.status_code}")

print("\nAll CRUD assertions passed")