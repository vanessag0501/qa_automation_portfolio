import requests 

BASE_URL = "https://jsonplaceholder.typicode.com"

# ── Schema validation — verify the shape of the response ─────────────
# This checks that all expected fields exist and are the right type

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
    print(f"  Schema valid for post ID {post['id']}")


#-- Test 1: SIngle Post Schema--
print("-- Test 1: Schema Validation --")
response = requests.get(f"{BASE_URL}/posts/1")
assert response.status_code == 200
validate_post_schema(response.json())

#Test 2: All posts schema
print("\n-- Test 2: All Posts Schema Validation --")
response = requests.get(f"{BASE_URL}/posts")
posts = response.json()

for post in posts:
    validate_post_schema(post)

print(f" All {len(posts)} posts passed schema validation!")

#-- Test 3: Filter by userID--
print("\n-- Test 3: Filter by userID --")
response = requests.get(f"{BASE_URL}/posts", params={"userId": 1})
filtered = response.json()

assert response.status_code == 200
assert len(filtered) > 0, "No posts returned for userId=1"
for post in filtered:
    assert post['userId'] == 1, f"Expected userId 1, got {post['userId']}"

print(f" All {len(filtered)} posts returned for userID - all correct")


#-- Test 4 : 404 Handling --
print("\n-- Test 4: 404 for missing resource--")

response = requests.get(f"{BASE_URL}/posts/9999") #this post doesn't exist
assert response.status_code == 404, f"Expected 404, got {response.status_code}"
print("  Correctly received 404 for missing post")

#-- Test 5: Response Headers -- 
print("\n-- Test 5: Response Headers --")
response = requests.get(f"{BASE_URL}/posts/1")
assert "application/json" in response.headers['Content-Type'], \
"Response is not JSON"

assert "Content-Type" in response.headers, "Missing content-type header"
print(f" Headers valid: {response.headers['Content-Type']}")

print("\nAll API assertions passed successfully!")
