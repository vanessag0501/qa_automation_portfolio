# DAY 27 — Data driven tests from CSV

import requests
import pytest
import csv
import os

BASE_URL = "https://jsonplaceholder.typicode.com"


# ── Step 1: Create the test data CSV ─────────────────────────────────
def create_test_data():
    filepath = "api_test_data.csv"
    with open(filepath, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["post_id", "expected_user_id", "expected_status"])
        writer.writerow(["1",  "1", "200"])
        writer.writerow(["2",  "1", "200"])
        writer.writerow(["5",  "1", "200"])
        writer.writerow(["50", "5", "200"])
        writer.writerow(["100","10","200"])
    return filepath


# ── Step 2: Load test data from CSV ──────────────────────────────────
def load_test_data(filepath):
    test_cases = []
    with open(filepath, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            test_cases.append((
                int(row["post_id"]),
                int(row["expected_user_id"]),
                int(row["expected_status"])
            ))
    return test_cases


# ── Step 3: Generate the CSV and load data ────────────────────────────
filepath  = create_test_data()
test_data = load_test_data(filepath)


# ── Step 4: Parametrize from CSV data ────────────────────────────────
@pytest.mark.parametrize("post_id, expected_user_id, expected_status", test_data)
def test_post_from_csv(post_id, expected_user_id, expected_status):
    response = requests.get(f"{BASE_URL}/posts/{post_id}")
    data = response.json()

    assert response.status_code == expected_status, \
        f"Post {post_id}: expected {expected_status}, got {response.status_code}"
    assert data["userId"] == expected_user_id, \
        f"Post {post_id}: expected userId {expected_user_id}, got {data['userId']}"
    assert data["id"] == post_id
    print(f"\n  Post {post_id} — userId {data['userId']} — OK")


# ── Step 5: CSV driven POST tests ─────────────────────────────────────
def create_post_data():
    filepath = "post_payloads.csv"
    with open(filepath, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["title", "user_id", "expected_status"])
        writer.writerow(["QA Test Post 1", "1", "201"])
        writer.writerow(["QA Test Post 2", "2", "201"])
        writer.writerow(["QA Test Post 3", "3", "201"])
    return filepath


post_filepath = create_post_data()
post_data = load_test_data = [
    row for row in csv.DictReader(open(post_filepath))
]


@pytest.mark.parametrize("row", post_data)
def test_create_post_from_csv(row):
    payload = {
        "title":  row["title"],
        "body":   "Generated from CSV",
        "userId": int(row["user_id"])
    }
    response = requests.post(f"{BASE_URL}/posts", json=payload)
    assert response.status_code == int(row["expected_status"])
    assert response.json()["title"] == row["title"]
    print(f"\n  Created: '{row['title']}' — ID {response.json()['id']}")