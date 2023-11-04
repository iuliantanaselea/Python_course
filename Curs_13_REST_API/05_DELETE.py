import requests
from pprint import pprint

URL = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.delete(URL)
if response.status_code == 200:
    data = response.json()
    pprint(data)
else:
    print(f" Request failed with status code {response.status_code}")