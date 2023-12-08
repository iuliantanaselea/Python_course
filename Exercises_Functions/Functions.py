"""
1.Funcție care să calculeze și să returneze suma a două numere

"""
from typing import Set


def sum(a, b):
    suma = a + b
    return suma


rezultat = sum(3, 5)
print(rezultat)

print('*' * 40)

"""
2. Funcție care să returneze TRUE dacă un număr este par, FALSE pentru impar
"""


def numar_par(numar):
    if numar % 2 == 0:
        return True
    else:
        return False


"""
3. Funcție care returnează numărul total de caractere din numele tău complet.
(nume, prenume, nume_mijlociu)
"""


def calcul_caractere(nume, prenume, nume_mijlociu):
    nume_complet = nume + prenume + nume_mijlociu
    return len(nume_complet)


rezultat = calcul_caractere('Mos', 'Ion', 'Roata')
print(rezultat)

"""
4. Funcție care returnează aria dreptunghiului
"""

"""
5. Funcție care returnează aria cercului
"""

import math


def calcul_aria_cerc(raza):
    aria = math.pi * raza ** 2
    return aria


rezultat = calcul_aria_cerc(1.8)
print(rezultat)

"""
6. Funcție care returnează True dacă un caracter x se găsește într-un string 
dat și False dacă nu găsește.
"""


def gaseste_caracter(caracter, string):
    if caracter in string:
        return True
    else:
        return False


rezultat = gaseste_caracter('b', 'abc')
print(rezultat)

"""
7. Funcție fără return, primește un string și printează pe ecran:
Numărul de caractere lower case este x
Numărul de caractere upper case exte y 
"""


def verificare_caractere(string):
    lower = 0
    upper = 0
    for caracter in string:
        if caracter.islower():
            lower += 1
        elif caracter.isupper():
            upper += 1
    print(f"Numar caractere lower: {lower}")
    print(f"Numar caractere upper: {upper}")


verificare_caractere('Ala Bala Portocala')

"""
8. Funcție care primește o LISTĂ de numere și returnează o LISTĂ doar cu numerele pozitive.
"""


def filtreaza_nr_pozitive(lista):
    numere_pozitive = []
    for numar in lista:
        if numar > 0:
            numere_pozitive.append(numar)
    return numere_pozitive


rezultat = filtreaza_nr_pozitive([1, -2, 3, 5, 7, -2, -1])
print(rezultat)
"""
9. Funcție care nu returneaza nimic. Primește două numere și PRINTEAZĂ
Primul număr x este mai mare decat al doilea număr y
Al doilea număr y este mai mare decat primul număr x
Numerele sunt egale. 
"""


def compara_numere(nr1, nr2):
    if nr1 > nr2:
        print(f"Primul numar {nr1} este mai mare decat al doilea numar {nr2}")
    elif nr2 > nr1:
        print(f"Al doilea numar {nr2} este mai mare decat primul numar {nr1}")
    else:
        print("Numerele sunt egale")


rezultat = compara_numere(4, 9)

"""
10. Funcție care primește un număr și un set de numere.
Printează ‘am adaugat numărul nou în set’ + returnează True
Printează ‘nu am adaugat numărul în set. Acesta există deja’ + returnează False
"""


# def adaugare_numar_in_set(numar, set):
#     if numar in set:
#         print(f"Nu am adaugat numarul {numar} in set. Acesta exista deja")
#         return False
#     else:
#         set.add(numar)
#         print(f" Am adaugat numarul {numar} nou in set")
#         return True
#

# set: set[int] = {0, 3, 5, 2, 4}
# rezultat = adaugare_numar_in_set(3, set)
# rezultat = adaugare_numar_in_set(6, set)

"""
11. Funcție care primește o lună din an și returnează câte zile are acea lună.
"""


def numar_zile_luna(luna):
    if luna == 2:
        return 28
    elif luna in [4, 6, 9, 11]:
        return 30
    else:
        return 31


numar_zile = numar_zile_luna(7)
print(numar_zile)

"""

12. Funcție calculator care să returneze 4 valori. Suma, diferența, înmulțirea, 
împărțirea a două numere.

În final vei putea face:
a, b, c, d = calculator(10, 2)
print("Suma: ", a)
print("Diferenta: ", b)
print("Inmultirea: ", c)
print("Impartirea: ", d)
"""


def calculator(a, b):
    suma = a + b
    diferenta = a - b
    inmultirea = a * b
    impartirea = a / b
    return suma, diferenta, inmultirea, impartirea


a, b, c, d = calculator(10, 3)
print("Suma: ", a)
print("Diferenta: ", b)
print("Inmultirea: ", c)
print("Impartirea: ", d)
"""
13. Funcție care primește o listă de cifre (adică doar 0-9) 
Exemplu: [1, 3, 1, 5, 9, 7, 7, 5, 5]
Returnează un DICT care ne spune de câte ori apare fiecare cifră
=> dict {
0: 0
1 :2
2: 0
3: 1
4: 0
5: 3
6: 0
7: 2
8: 0
9: 1
}

"""


def frecventa_cifre(lista):
    frecventa = {} #initializam un dictionar gol
    for cifra in lista: #parcurgem fiecare cifra din lista de intrare
        if cifra not in frecventa: #verificam daca cifra nu a fost intalnita pana acum in dictionar
            frecventa[cifra] = 1 #daca cifra e intalnita prima data adauga 1
        else:
            frecventa[cifra] += 1 #daca a fost gasita de mai multe ori adauga +1
    for cifra in range(10): #parcurge cifrele de la 0 la 9 pentru a completa dictionarul
        if cifra not in frecventa: #daca cifra lipseste o adaugam in dictionar cu valoarea 0
            frecventa[cifra] = 0
    return frecventa #afiseaza dictionarul

lista_cifre = [1, 3, 1, 5, 9, 7, 7, 5, 5]
print(frecventa_cifre(lista_cifre))



"""
14. Funcție care primește 3 numere. Returnează valoarea maximă dintre ele.
"""
def gaseste_maxim(a,b,c):
    return max(a,b,c)

rezultat = gaseste_maxim(1,4,5)
print(rezultat)

"""
15. Funcție care să primească un număr și să returneze suma tuturor numerelor de la 
0 la acel număr.
Exemplu: dacă dăm numărul 3, suma va fi 6 (0+1+2+3)
"""

def suma_numere_mai_mici(numar):
    suma = 0
    for i in range(numar+1):
        suma +=i
    return suma
rezultat = suma_numere_mai_mici(5)
print(rezultat)
"""

16.Funcție care primește 2 liste de numere (numerele pot fi dublate). Returnați numerele comune.

Exemplu:
list1 = [1, 1, 2, 3]
list2 = [2, 2, 3, 4]
Răspuns: {2, 3}
"""
lista1 = [1, 1, 2, 3]
lista2 = [2, 2, 3, 4]
def numere_comune(lista1, lista2):
    set_lista1 = set(lista1)
    set_lista2 = set(lista2)
    numere_comune = set_lista1.intersection(set_lista2)
    return numere_comune

rezultat = numere_comune(lista1,lista2)
print(rezultat)
"""
17. Funcție care să aplice o reducere de preț.
Dacă produsul costă 100 lei și aplicăm reducere de 10%. Pretul va fi 90 de lei.
Tratează cazurile în care reducerea e invalidă. De exemplu o reducere de 110% e invalidă.
"""
def reducere_pret(reducere, pret):
    if reducere<100 and reducere>0:
        # pret_redus = pret - reducere/100*pret
        pret_redus = pret * (1- reducere/100)
        return pret_redus
    else:
        print("Reducerea este invalida")
        return None
pret_initial = 100
reducere = 10
pret_redus = reducere_pret(reducere,pret_initial)
print (pret_redus)
"""
 18.Funcție care să afișeze data și ora curentă din România.
(bonus: afișazăi și data și ora curentă din China)
"""
import datetime
import pytz
import time
def afiseaza_data_ora():
    fus_orar_Romania = pytz.timezone('Europe/Bucharest')
    data_ora_Romaniei = datetime.datetime.now(fus_orar_Romania)
    print("Data si ora in Romania este:", data_ora_Romaniei)
    fus_orar_China = pytz.timezone('Asia/Shanghai')
    data_ora_Chinei = datetime.datetime.now(fus_orar_China)
    print("Data si ora in China este:", data_ora_Chinei)
afiseaza_data_ora()

# for i in range(5):
#     afiseaza_data_ora()
#     time.sleep(4)

