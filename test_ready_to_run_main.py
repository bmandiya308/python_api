import requests

BASE = "http://127.0.0.1:5000"


def print_response(label, response):
    print(f"\n{label}")
    print("status:", response.status_code)
    try:
        print("body:", response.json())
    except ValueError:
        print("body:", response.text)


# Make sure the app is running first.
try:
    response = requests.get(f"{BASE}/getid/1", timeout=5)
    print_response("HEALTH CHECK /getid/1", response)
except requests.exceptions.RequestException as e:
    print("The Flask app is not running.")
    print("Start it with: python main.py")
    print("Error:", e)
    raise SystemExit(1)

# 1) GET a record that does not exist yet
response = requests.get(f"{BASE}/getid/1", timeout=5)
print_response("GET missing id=1", response)

# 2) Create a valid book with JSON payload
payload = {
    "id": 1,
    "title": "Report Card",
    "author": "Dinkar jani",
    "first_sentence": "This is a sample book entry.",
    "published": 2020,
}
response = requests.post(f"{BASE}/getid/1", json=payload, timeout=5)
print_response("POST create id=1", response)

# 3) GET the created record
response = requests.get(f"{BASE}/getid/1", timeout=5)
print_response("GET created id=1", response)

# 4) PATCH update the created record
response = requests.patch(f"{BASE}/getid/1", json={"author": "Updated Author"}, timeout=5)
print_response("PATCH update id=1", response)

# 5) GET again to confirm the update
response = requests.get(f"{BASE}/getid/1", timeout=5)
print_response("GET updated id=1", response)

# 6) DELETE the record
response = requests.delete(f"{BASE}/getid/1", timeout=5)
print_response("DELETE id=1", response)

# 7) Confirm the book is gone
response = requests.get(f"{BASE}/getid/1", timeout=5)
print_response("GET after delete id=1", response)
