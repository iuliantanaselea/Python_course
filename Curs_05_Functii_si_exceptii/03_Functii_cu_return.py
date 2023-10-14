def say_hi():
    return "Hello"
text = say_hi()
print(text)

def suma(a,b,c):
    return a+b+c

print (suma(1,2,3))

def show_biggest(a,b):
    if a>b:
        print(a)
    else:
        print(b)

b = show_biggest(1,2) #Daca nu specificam o valoare de retur pentru functia ea va returna implicit None
print(b)

def nimic():
    return #return fara o valoare dupa el inseamna return none

print(nimic())

def end():
    return 1
    print('Hello') #bucata aceasta de cod nu se va rula pt ca toate functiile se opresc cand dau de cuvantul return

print(end())

#Exercitiu
#Sa se scrie o functie care primeste ca parametru o lista de numere si returneaza o lista care contine doar numerele pare

def get_all_even_numbers(numbers):
    result = []
    for elem in numbers:
        if elem % 2 == 0:
            result.append(elem)
    return result
lista = [1,4,5,7,8,9,2]
print(get_all_even_numbers(lista))

