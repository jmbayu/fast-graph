import requests

url = "http://127.0.0.1:8000/auth/launch_user"
payload = {
  "username": "john",
  "password": "secretPassw",
  "application_password": "secure_this_PASS",
  "full_name": "John Doe"
}

response = requests.post(url, params=payload)

print(response.status_code)
print(response.json())