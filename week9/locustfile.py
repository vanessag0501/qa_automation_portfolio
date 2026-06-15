from locust import HttpUser, task, between

class JSONPlaceholderUser(HttpUser):
    host = "https://jsonplaceholder.typicode.com"
    wait_time = between(1, 3)

    @task(2)
    def get_posts(self):
        self.client.get("/posts", name="GET /posts")

    @task(1)
    def get_single_post(self):
        self.client.get("/posts/1", name="GET /posts/1")

    @task(1)
    def create_post(self):
        self.client.post("/posts", json={
            "title": "test post",
            "body": "performance test",
            "userId": 1
        }, name="POST /posts")