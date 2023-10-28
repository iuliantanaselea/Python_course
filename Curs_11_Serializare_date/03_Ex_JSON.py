"""
JSON -> JavaScript Object Notation
    -->seamana cu o lista de dictionare
    -> se foloseste la transfer de date
"""
import json
from pprint import pprint

def read():
    with open("angajati.json", "r") as f:
        return json.load(f)

l= read()
pprint(l)

def write(d):
    with open("angajati2.json", "w") as f:
        json.dump(d,f, indent = 4)

data = [
   {"Nume": "Sergiu", "Varsta": "24"},
   {"Nume": "Andrei", "Varsta": "31"},
   {"Nume": "Dan", "Varsta": "22"},
   {"Nume": "Ioana", "Varsta": "20"}
]

write(data)