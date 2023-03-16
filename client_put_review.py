import requests

REVIEW_ID = 5
URL = f'http://localhost:8000/api/v1/reviews/{REVIEW_ID}'

REVIEW = {
    'review': 'Review modificada con request',
    'score': 5
}

response = requests.put(URL, json=REVIEW)

if response.status_code == 200:
    print('La reseña se actualizo correctamente')

    print(response.json())