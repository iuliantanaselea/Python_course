import requests
from pprint import pprint

URL = "https://jsonplaceholder.typicode.com/posts?userId=2&_limit=2"
response = requests.get(URL)
if response.status_code == 200:
    data = response.json()  # transformam raspunsul din format JSON in dictionar {}
    pprint(data)
else:
    print(f" Request failed with status code {response.status_code}")

