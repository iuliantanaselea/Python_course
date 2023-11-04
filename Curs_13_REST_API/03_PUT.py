import requests
from pprint import pprint
"""
# !! Metoda PUT da overwrite la itnregul obiect astfel ca s-ar putea sa-i stearga anumite date
Daca vrem sa pastram toate datele anterioare:
    1 pastram in payload datele pe care nu vrem sa le modificam
    2 folosim metoda PATCH
"""
URL = "https://jsonplaceholder.typicode.com/posts/1"
payload = payload = {'title': 'poo'}
response = requests.put(URL, json=payload)
if response.status_code==200:
    data = response.json()
    pprint(data)
else:
    print(f" Request failed with status code {response.status_code}")