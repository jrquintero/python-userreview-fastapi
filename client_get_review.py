import requests

REVIEW_ID = 5
URL = f'http://localhost:8000/api/v1/reviews/{REVIEW_ID}'

response = requests.get(URL)

if response.status_code == 200:
    print(response.json())
else:
    print(response.content)