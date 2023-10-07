#Lista de elemente - list

"""
-o insiruire de elemente ordonate
-pot avea valori diferite
-este MUTABILA (MUTABLE) : se pot adauga, sterge sau inlocui elemente din lista
- putem accesa orice index
-putem pune valori repetabile
- se defineste intre []
"""

lista_diversa = [2, 3.14, False, 'Elefant', 12345] #Indes 0:4 (4 ultimul index)
print(f"lista_diversa: {lista_diversa}")

#Accesam elementul al 2-lea:
element2 = lista_diversa[1]
print(f"element2: {element2}")

ultimul_element = (lista_diversa[-1])  #Ultimul element din lista
print(f"ultimul element: {ultimul_element}")

penultimul_element = (lista_diversa[-2])  #Penultimul element din lista
print(f"penultimul element: {penultimul_element}")

# Verificam ce lungime are lista:
lungime_lista = len(lista_diversa)
print(f' lungime lista: {lungime_lista}')

#Incercam sa accesam un element care depaseste lungimea listei:
#
# un_element = lista_diversa[6]
# print(f'Elementul 6: {un_element}')

print("-"*30)

## OPERATII cu ELEMENTE

#Inlocuirea / Schimbarea unui element din lista
lista_diversa[2] = True #am modificat-o datorita proprietatii de mutabilitate (este mutabila)
print(f"lista_diversa: {lista_diversa}")

print("-"*30)

#Adaugarea unui nou element intr-o lista
#La coada: se face cu append
lista_diversa.append('hasta la vista')
print(f"lista_diversa: {lista_diversa}")

#in interiorul listei: se face cu insert
lista_diversa.insert(3, 10*10)
print(f"lista_diversa: {lista_diversa}")

# Stergerea ultimului element din lista :
lista_diversa.pop() # Daca nu scrii nimic intre paranteze, sterge ultimul element
print(f"lista_diversa: {lista_diversa}")

#Stergerea unui element pe baza de index:
lista_diversa.pop(2)
print(f"lista_diversa: {lista_diversa}")

print("-"*30)

# LIST SLICING
# Inversarea listei:
lista_inversa = lista_diversa[::-1]
print(f"lista_inversa: {lista_inversa}")

# parte din lista:
# ultimele 3 elemente din lista:
print(f"lista_inversa ultimele 3 elemente: {lista_inversa[-3:]}")