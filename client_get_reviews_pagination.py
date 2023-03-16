import requests

URL = 'http://localhost:8000/api/v1/reviews'
# URL = 'http://localhost:8000/api/v1/reviews?page=2&limit=1'
HEADERS = { 'accept': 'application/json' }
QUERYSET = { 'page': 2, 'limit': 1 }


response = requests.get(URL, headers=HEADERS, params=QUERYSET)

if response.status_code == 200:
    print('Peticion realizada con exito')
    print('\n')
    # print(response.content)
    # print('\n')
    # print(response.headers)

    if response.headers.get('content-type') == 'application/json':
        # print(response.json())
        reviews = response.json()
        for review in reviews:
            print(f"score: {review['score']} - {review['review']} ")