"""
csv - comma separated values
    - folosite pentru stocare date/rapoarte
"""

import csv
from pprint import pprint


# Citire, scriere folosind liste
def read():
    with open("angajati.csv", "r") as f:
        reader = csv.reader(f)
        angajati = []
        for row in reader:
            angajati.append(row)
        return angajati


l = read()
pprint(l)

print('-' * 30)


def write(d):
    with open("persoane.csv", 'w', newline="") as f:
        writer = csv.writer(f)
        writer.writerows(d)


data = [
    ["Nume", "Varsta"],
    ["Sergiu", "25"],
    ["Andrei", "30"],
    ["Cristi", "34"]
]
write(data)
print('-' * 30)


# Citire/scriere folosind dictionar

def read_dict():
    with open("angajati.csv", "r") as f:
        reader = csv.DictReader(f) #DictReader stie ca primul rand contine cheile
        angajati = []
        for row in reader:
            angajati.append(row)
        return angajati


l = read_dict()
pprint(l)

print('-' * 30)

def write_dict(d):
    with open("persoane2.csv", 'w', newline="") as f:
        writer = csv.DictWriter(f,fieldnames=d[0].keys()) #trebuie sa specificam unde sunt cheile
        writer.writeheader()#scriem capul de tabel
        writer.writerows(d)

data2=[
    {"Nume": "Sergiu", "Varsta": "25"},
    {"Nume": "Andrei", "Varsta": "31"},
    {"Nume": "Dan", "Varsta": "45"}

]
write_dict(data2)