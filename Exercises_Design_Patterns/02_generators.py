"""
Generators

Implementați un generator pentru loteria 6/49 și noroc:
Primele 6 apelări către generator vor da cate un numar intre 1 si 49 (inclusiv
Ultima apelare va da un singur număr de “noroc” format din 7 cifre
"""

import random

def LotoGenerator():
    lista = random.sample(range(1,50),6) # sample se asigura ca nu avem duplicate in lista
    #aici am generat o lista de k numere intre 1 si 49 fara a avea duplicate
    for i in lista:
        yield i
    yield random.randint(1_000_000,9_000_000)

for val in LotoGenerator():
    print (val)

print("-"*30)

#Varianta 2
def LotoGenerator2():
    lista2 = []
    for i in range(6):
        numar = random.randint(1,50)
        while numar in lista2:
            numar = random.randint(1,50)
        lista2.append(numar)
        yield numar
    yield random.randint(1_000_000, 9_000_000)

print(LotoGenerator())
print(LotoGenerator2())
for numar in LotoGenerator2():
    print(numar)

print("-"*30)

