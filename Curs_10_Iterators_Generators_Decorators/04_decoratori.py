'''
    - Decoratorii : sunt combinarea a trei concepte
    - Decoratoarele sunt niste tool-uri foarte puternice in Python pentru ca permit programatorilor
sa modifice comportamentul initial al unei functii sau a unei clase.
    - Decoractoarele ne permit sa creeam un wrapper peste o alta functie pentru a-i extinde
comportamentul, fara a-i schimba implementarea originala.

Ex:
De exemplu, sa presupunem ca am dori sa masuram cat de eficient se executa functiile/metodele
noastre, am dezvolta un decorator care masoara timpul si l-am pune peste functionalitatea noastra
'''


# Functii ca argumente
def say_hello(name):
    return f'Hello {name}'


def say_hi(name):
    return f'Hi {name}'


def greet_bob(func):
    return func('Bob')


print(greet_bob(say_hello)) #daca nu punem () dupa say_hello, nu apelam functia ci doar o pasam
print(greet_bob(say_hi))

print('*' * 30)


# Functii interne

def parent():
    def first():  # se pot defini functii in interiorul altor functii
        print('Hello from first')

    def second():
        print('Hello from second')

    second()
    first()


parent()
print('*' * 30)


# Returnare de functii

def parent(n):
    def first():
        print('First')

    def second():
        print('Second')

    if n == 1:
        return first #important: FARA PARANTEZE.
                     # Astfel returnam referinta catre functie nu rezultatul ei
    return second


f = parent(1)  # f -> este o functie interna
f()
print('*' * 30)

# Decoratori simpli
import functools


def my_decorator(func):
    @functools.wraps(func)  # Se adauga pentru a nu se suprascrie functia decorata cu
    # functia wrapper
    def wrapper():
        print('Ceva se inampla inainte de apelul functiei decorate')
        func()
        print('Ceva se intampla dupa apelul functiei decorata')

    return wrapper


@my_decorator #astfel inlocuim functia de mai jos cu functia wrapper
def say_we():
    print('We')


say_we()
print(say_we)
print('*' * 30)


# Decoratori pentru functii cu argumente

def do_twice(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs): #pentru ca functia are argumente, trebuie completate parantezele
        func(*args, **kwargs)
        func(*args, **kwargs)

    return wrapper

@do_twice #cu @ decoram functia cu decoratorul do_twice
def say_salut(name):
    print(f'Salut {name}')


say_salut('Bob')
