#DICT - DICTIONARUL - {}
"""
- dictionarul este o colectie de date de tip cheie-valoare (fiecare cheie are o valoare)
- dictionarul in sine este MUTABIL
- cheile (keys) sunt unice !
- valoarile (values) se pot repeta
- cheile trebuie sa fie IMMUTABLE ( doar de tip: int, str, tuple)
"""

# initializare dictionar
persoana = {
    'nume':'Stefan',
    'prenume':'Gheorghiu',
    'varsta':47
}
print(f"Persoana = {persoana}")

# adaugarea unui element in dictionar
persoana['initiala_tatalui'] = 'P'
print(f"Persoana = {persoana}")

# Modificarea unui element existent (folosesc cheia pe care o doresc)
persoana['initiala_tatalui'] = 'Y'
print(f"Persoana = {persoana}")

# Stergere elemente:
persoana.pop('initiala_tatalui')
print(f"Persoana = {persoana}")

print("-"*30)

#Accesarea unui elem non-existent => eroare (ca si la set)
print(f"valoarea cheii unui element din persoana: {persoana['varsta']}")
# print(f"valoarea unui element din persoana: {persoana['var']}") #KeyError: 'var'

#lungimea disctionarului
lungime_dictionar= len(persoana)
print(f"lungime dictionar: {lungime_dictionar}")

