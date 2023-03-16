import requests

URL = 'http://localhost:8000/api/v1/users/'
USER = {
    'username': 'jquintero',
    'password': '123456'
}

response = requests.post(URL + 'login', json=USER)

if response.status_code == 200:
    print('Usuario autenticado')

    # print(response.json())
    # print(response.cookies) # RequestsCookieJar
    # print(response.cookies.get_dict())

    user_id = response.cookies.get_dict().get('user_id')
    # print(user_id)

    cookies = { 'user_id': user_id }
    response = requests.get(URL + 'reviews', cookies=cookies)

    if response.status_code == 200:
        for review in response.json():
            print(f"{review['review']} - {review['score']}")
else:
    print(response.content)