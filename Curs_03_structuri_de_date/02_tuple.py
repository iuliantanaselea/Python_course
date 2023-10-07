## TUPLE - (tuplu)
"""
- tuple este un tip de date IMUTABIL (NU SE POT sterge, adauga, modifica valori in interiorul ei)
- sunt valori ordonate si indexabile
- pot exista mai multe valori repetate
"""

#Definim un tuple - ()
tuple_numere = (1,2,3)
print(f'tuple numere: {tuple_numere}')

# nu se pot schimba valori => imposibil
# tuple_numere[-1] = 4

print("-"*40)

lista_litere = ['a', 'b', 'c', 'a']
print(f" lista litere: {lista_litere}")
lista_litere.append('d')
print(f" lista litere: {lista_litere}")


#Transform o lista intr-un tuple :
tuple_litere = tuple(lista_litere)
print(f" tuple litere: {tuple_litere}")

print("-"*40)

#Pot sa le numar si sa le accesez cu index
elem1 = tuple_litere[0]
print(f"Primul element: {elem1}")
print(f"verific lungime tuple: {len(tuple_litere)}")
print(f"numar cate elemente sunt in tuple: {tuple_litere.count('a')}")

print("-"*40)