"""
1. Explică cu cuvintele tale în cadrul unui comentariu cum funcționează un if else.

Raspuns: Este o structura care controleaza si permite o executare diferita a codului in functie de evaluarea unei conditii.
"""
"""
2. Verifică și afișează dacă x este număr natural sau nu.
"""
"""
x=int(input("Introdu un numar: ")) #citire numarului de la tastatura

if x >= 1 :
    print(f"{x} este un numar natural")
else:
    print(f"{x} nu este un numar natural")
"""

"""
3. Verifică și afișează dacă x este număr pozitiv, negativ sau neutru.
"""
"""
x=float(input("Introdu un numar: ")) #citire numarului de la tastatura

if x > 0 :
    print(f"{x} este un numar pozitiv")
elif x < 0 :
    print(f"{x} este un numar negativ")
else:
    print(f"{x} este un numar neutru")
"""

"""
4. Verifică și afișează dacă x este între -2 și 13.
"""
"""
x=float(input("Introdu un numar: ")) #citire numarului de la tastatura
#if x> -2 and x< 13:
if -2 < x < 13:
    print(f"{x} se afla in intervalul (-2, 13).")
else:
    print(f"{x} nu se afla in intervalul (-2, 13).")
x = int(input('Numar: '))
rezultat =  "Numarul este in interval" if -2 < x < 13 else "Numarul este in afara intervalului"
print(rezultat)
"""

"""
5. Verifică și afișează dacă diferența dintre x și y este mai mică de 5.
"""

"""
x=int(input("x= ")) #citire numarului de la tastatura
y=int(input("y= ")) #citire numarului de la tastatura
z=abs(x-y) #calcularea valorii absolute a diferentei
if z<5:
    print(f"Diferenta dintre {x} si {y} este mai mica decat 5")
else:
    print(f"Diferenta dintre {x} si {y} este mai mare decat 5")
"""


"""
6. Verifică dacă x NU este între 5 și 27  - a se folosi ‘not’.
"""
"""
x=int(input("Introdu un numar: "))

if not(x <= x <= 27):
    print(f"{x} nu se afla intre 5 si 27")
else:
    print(f"{x} se afla intre 5 si 27")
"""


"""
x și y (int)
Verifică și afișează dacă sunt egale, dacă nu afișează care din ele este mai mare.

"""
"""
x=int(input("x= ")) #citire numarului de la tastatura
y=int(input("y= ")) #citire numarului de la tastatura
if x==y:
    print(f"{x} este egal cu {y}")
elif x>y:
    print(f"{x} este mai mare decat {y}")
else:
    print(f"{x} este mai mic decat {y}")
"""


"""
8. 
X, y, z - laturile unui triunghi.
Afișează dacă triunghiul este isoscel, echilateral sau oarecare.

"""
x=int(input("x= "))
y=int(input("y= "))
z=int(input("z= "))
if x == y == z:
    print("triunghiul este echilateral")
elif x == y or y == z or x == z:
    print("triunghiul este isoscel")
else:
    print("triunghiul este oarecare")

