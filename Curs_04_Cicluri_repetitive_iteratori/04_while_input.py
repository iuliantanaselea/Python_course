"""
Program care verifica inputul de la tastatura

"""

"""
DEFINIREA EXACTA A PROBLEMEI:
1. Verificam ca inputul de la tastatura sa fie de tip int, moment in care sa se opreasca
2. Daca nu este de tip int, continua bucla while (la nesfarsit)

"""

# numar = 10 #int
# while True:
#     numar = input("prompter:")
#     if numar.isnumeric():
#         print(f"Da, acesta este un numar")
#         break
#     else:
#         print(f"Imi pare rau, {numar} nu este un numar")

"""
DEFINIREA EXACTA A PROBLEMEI:
1. Verificam ca inputul de la tastatura sa fie de tip FLOAT, moment in care sa se opreasca
2. Daca nu este de tip int, continua bucla while (la nesfarsit)

"""


while True:
    numar = input("prompter:")
    if numar.isnumeric() or  numar.count('.') == 1 and numar.replace('.', '0').isnumeric():
        print(f"Da, acesta este un numar")
        break
    else:
        print(f"Imi pare rau, {numar} nu este un numar")