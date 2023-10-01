# TIPURI DE VARIABILE

# variabila de tip "int" ( numar intreg)
a = 12
b = -16

# variabila de tip FLOAT (nr. zecimal)
pi = 3.14159

# variabila de tip STRING (sir de caractere)
# intodeauna intre ghilimele duble sau simple

d = "Ana are mere parametrice 1234!@!#$!%&^%$)(*&^%$ TEST"
e = 'Ana are mere '
# e = Ana are mere # nu e corect definita pentru ca nu are " "

#variabila de tip "BOOLEAN" (valori adevarat/fals)

f = True
g = False

# Acesta este un comentariu pe o singura linie
# Alt comentariu pe o linie


"""Acesta este un comentariu
Pe mai multe linii
Folosim ghilimele triple
Simple sau duble"""

'''Hai sa facem
Cu ghilimele simple'''


# Asignare MULTIPLA DE VARIABILE
# variabilele sunt mereu cu litere mici si "_" daca e nume compus
mama , tata = "Oana" , "George"
varsta_mama = 40

# TIPURI DE PRINT

print(mama) # Daca vreau sa printez numai variabile nu am nevoie de ghilimele
print("Pe mama o cheama: ",mama , "; Pe tata il cheama:" , tata) # la printare de variabile nu se folosesc ghilimele
print("Pe mama o cheama: " +mama +  "; Pe tata il cheama:"  + tata) # "+" elimina spatiu, fata de ","
print("Pe mama o cheama: " + mama + " " + str(varsta_mama))
print(f"Pe mama o cheama {mama} si are {varsta_mama} ani") # {} includ variabila in cadrul "". "f" din print = formating
