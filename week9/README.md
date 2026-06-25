# Week 9 - Performance Testing

Load testing with Locust against a live REST API.

## Contents
- `locustfile.py` - defines virtual user scenarios (GET list, GET single, POST) with weighted tasks
- `load_test_results.csv` - exported results from a sample run

## Target
Tests run against jsonplaceholder.typicode.com.

## Running
```
python -m locust -f locustfile.py
```
Then open http://localhost:8089 to set the number of users and spawn rate and start the test.