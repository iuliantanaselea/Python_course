ske = ('-' * 44)
print(ske)

"""
Generator = Un obiect care poate crea valori care pot fi parcurse secvential asemanator unui
            iterator, dar sunt implementati sub forma de functii
        
        ! Generatorii sunt acele functii care nu folosesc 'return' pentru a se opri dand inapoi
        o valoare, ci folosesc cuvantul 'yield' pentru a ceda o valoare, dupa care va putea reveni
        in aceiasi functie sa continue executia
"""


def gen():
    print('Am intrat in functia generator')
    yield 10  # yield = a ceda

    print('Am intrat din nou in functia generator')
    yield 100

    print('Am intrat a treia oara in functia generator')


g = gen()
print(next(g))
print(next(g))
# print(next(g)) ---> # ca sa nu returneze eroarea StopIteration

print(ske)


def even_gen(n):
    generated_numbers = 0
    current = 0
    while generated_numbers < n:
        current += 1
        if current % 2 == 0:
            yield current
            generated_numbers += 1


g2 = even_gen(10)
for i in g2:
    print(i)

print(ske)
