class CustomException(Exception):  # preia toate atributele din clasa Exception
    pass


"""
Sa se scrie o functie  care ferifica daca o lista de numere intregi primite ca parametru
contine numere negative. Daca da, sa se arunce o exceptie specifica.
"""


class ContainsNegativeNumbersException(Exception):
    pass


def verify_negative_numbers(numbers):
    for number in numbers:
        if number < 0:
            raise ContainsNegativeNumbersException(f" contine {number}")


verify_negative_numbers([1, 3, -3, -2, 4])
