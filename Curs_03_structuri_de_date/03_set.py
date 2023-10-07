# SET (Setul) - {}
"""
- setul este o colectie de elemente UNICE (nu pot avea valori duplicate)
- elementele pot fi de tipuri diferite
- nu este ordonat
- este MUTABIL ( adaugam, stergem, atat) !NU putem modifica alemente
- fiecare element din set trebuie sa fie IMUTABIL
- valorile setului fiind unice sunt considerate ca si chei (keys)
- un set gol se defineste : set()
"""

# cream un set:
data_curenta = {2023,'iulie', 11, True, 19, 49, 'PM'}
print(f"Data curenta: {data_curenta}")

print("-"*30)

# Adaugam o valoare:
data_curenta.add(2022)
print(f"Data curenta: {data_curenta}")

# Adaugam un tuple:
data_curenta.add((7,8,9))
print(f"Data curenta: {data_curenta}")

print("-"*30)

#Stergem un element existent:
data_curenta.remove(2022)
print(f"Data curenta: {data_curenta}")
# eroare in caz ca cheia nu exista

print(f"Lungime set data curenta: {len(data_curenta)}")