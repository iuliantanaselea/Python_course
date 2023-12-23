def logger(func):
    def wrapper(*args, **kwargs):
        print(f'Date intrare args {args}')
        print(f'Date intrare kwargs {kwargs}')
        result = func(*args, **kwargs)
        print(f'Date iesire {result}')
        return result

    return wrapper


@logger
def suma(a, b):
    return a + b


@logger
def suma2(a, b, c):
    return a + b + c


suma(a=3, b=5)
suma(4, 5)
suma2(4, 7, c=8)
suma2(7,8,9)

