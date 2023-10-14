def plus(a, b=2):
    return a + b


plus(1)  # daca nu spcificam o valoare implicita pentru b atunci va lua valoarea implicita 2
plus(1, 3)


###############################

# Keyword arguments (argumente cu nume)
def plus_keyword(a, b):
    return a + b


plus_keyword(a=1, b=2)
plus_keyword(b=2, a=1)  # Specificand argumentele prin nume, nu mai este necesar sa pastram ordinea lor


####################################################
# Variable number of arguments (numar variabil de argumente)

def plus_many(*args):  # ia toate argumentele si le pune intr-un tuplu
    print(args)
    return sum(args)


plus_many(1, 2, 3)

plus_many()
plus_many(*[1, 2, 3])  # steluta se mai numeste unpacking, nu putem pune argumente cu nume


def plus_many_2(**kwargs):  # ia toate argumentele si le pune intr-un dictionar
    print(kwargs)
    return sum(kwargs.values())


plus_many_2(a=1, b=2)
plus_many_2(k=5, y=17)


def plus_many_3(*args, **kwargs):
    print(args, kwargs)
    return sum(args) + sum(kwargs.values())


plus_many_3(1, 2, 3, a=8, b=3)
plus_many_3(1, 2)
plus_many_3(a=3, b=9)
plus_many_3()
print(plus_many_3(1, 2, 3, a=9, b=3))
# plus_many_3(a=1,3) # parametrii pozitionali pot fi pusi doar inainte de cei cu nume
