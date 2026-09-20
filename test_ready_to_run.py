import time

import requests

BASE = "http://127.0.0.1:5000"
BOOK_ID = int(time.time())


def print_response(label, response):
    print(f"\n{label}")
    print("status:", response.status_code)
    try:
        print("body:", response.json())
    except ValueError:
        print("body:", response.text)


# Make sure the app is running first.
try:
    response = requests.get(f"{BASE}/getid/{BOOK_ID}", timeout=5)
    print_response(f"HEALTH CHECK /getid/{BOOK_ID}", response)
except requests.exceptions.RequestException as e:
    print("The Flask app is not running.")
    print("Start it with: python main.py")
    print("Error:", e)
    raise SystemExit(1)

# 1) GET a record that does not exist yet
response = requests.get(f"{BASE}/getid/{BOOK_ID}", timeout=5)
print_response(f"GET missing id={BOOK_ID}", response)

# 2) Create a book with a JSON payload
payload = {
    "title": "Report Card",
    "author": "Dinkar Jani",
    "first_sentence": "This is a sample book entry.",
    "published": 2020,
}
response = requests.post(f"{BASE}/getid/{BOOK_ID}", json=payload, timeout=5)
print_response(f"POST create id={BOOK_ID}", response)

# 3) GET the created book
response = requests.get(f"{BASE}/getid/{BOOK_ID}", timeout=5)
print_response(f"GET created id={BOOK_ID}", response)

# 4) Update the book
response = requests.patch(
    f"{BASE}/getid/{BOOK_ID}",
    json={"author": "Updated Author"},
    timeout=5,
)
print_response(f"PATCH update id={BOOK_ID}", response)

# 5) GET again to confirm the update
response = requests.get(f"{BASE}/getid/{BOOK_ID}", timeout=5)
print_response(f"GET updated id={BOOK_ID}", response)

# 6) DELETE the book
response = requests.delete(f"{BASE}/getid/{BOOK_ID}", timeout=5)
print_response(f"DELETE id={BOOK_ID}", response)

# 7) Confirm deletion
response = requests.get(f"{BASE}/getid/{BOOK_ID}", timeout=5)
print_response(f"GET after delete id={BOOK_ID}", response)
