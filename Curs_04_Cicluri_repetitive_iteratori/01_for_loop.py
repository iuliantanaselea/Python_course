"""

ITERATORI (BUCLE REPETITIVE)

- este un obiect care poate fi iterat (parcurs un element cate un element, unu cate unu)
Ex: lista, tuple, set, dict, string
    (nu pot fi iterate: Bool, Int, Float)

-contin un numar de valori care se pot numara (itera)
"""

fructe = ['mar', 'para', 'banana', 'portocala', 'cireasa']
print(f" fructe: {fructe}")

print("-"*40)
for fruct in fructe:
    print(fruct, end= ' ') # PRINTEAZA PE UN SINGUR RAND

print('\n',"-" * 40) #\n - new line (linie noua)

for fructul_meu in fructe: #for poate avea else la sfarsit ca si alternativa de terminare
    print(f"fructul_meu= {fructul_meu}")
else:
    print("Am terminat bucla repetitiva for.") # (este o Particularitate Python)

print("-"*40)

lista_mixta = ['avocado', 2023, True, 5.66, 'Mihai', (11,12)]

for elem in lista_mixta:
    if type(elem) is str:
        elem = elem.upper()
        print(elem)
    else:
        print(f"{elem} nu este string")

print("-"*40)

# ITERATIE LA NUMERE:

for numar in range(1,11,2): # la functia range: ultimul numar nu este accesat. range(inceput, final+1, pas)
    print(numar)

print("-"*40)

for numar in range(10,0,-1): #parcurgem descrescator
    print(numar, end=' ')
print()

#cea mai simpla iteratie posibila:
for i in range(5):
    print(i)