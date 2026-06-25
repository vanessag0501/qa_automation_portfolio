# Week 8 - Postman and Newman

API collection testing with Postman, run from the command line with Newman and wired into CI.

## Contents
- `jsonplaceholder_collection.json` - a Postman collection with assertions across multiple endpoints
- `jsonplaceholder_env.json` - the environment file with the base URL variable

## Running
Requires Newman (`npm install -g newman`).
```
newman run jsonplaceholder_collection.json -e jsonplaceholder_env.json
```