import requests
from pprint import pprint

URL = "https://jsonplaceholder.typicode.com/posts?userId=2&_limit=2"
payload = {'title': 'poo', 'body': 'var', "userId": 2}  # postarea pe care noi vrem sa o adaugam in baza de date sau server
response = requests.post(URL, json=payload)

if response.status_code == 201:
    data = response.json()
    pprint(data)
else:
    print(f" Request failed with status code {response.status_code}")
