"""
Decorators
Implementați următorii decoratori:
timeit – decorator care măsoară timpul de execuție al unei funcții
logger – decorator care printeaza argumentele de intrare, și rezultatul unei funcții

"""
import time
import functools
def timeit(func):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        rezultat = func(*args,**kwargs)
        stop_time = time.time()
        print(f'Functia {func.__name__} a rulat in {stop_time-start_time:.5f} secunde')
        # func.__name__ ->afiseaza numele functiei
        return rezultat
    return wrapper

def logger(func):
    def wrapper(*args, **kwargs):
        print(f'Date intrare args {args}')
        print(f'Date intrare kwargs {kwargs}')
        result = func(*args, **kwargs)
        print(f'Date iesire {result}')
        return result

    return wrapper


def salut(func):
    @functools.wraps(func)
    def wrapper2(*args,**kwargs):
        print("Salut")
        return func(*args,**kwargs)
    return wrapper2 # ! FARA PARANTEZE. Adica declaram neapelat

@logger
# @timeit
# @salut
def descrie_vremea(grade):
    time.sleep(2)
    return f"Vremea e frumoasa, sunt {grade} de grade"


print(descrie_vremea(30))

