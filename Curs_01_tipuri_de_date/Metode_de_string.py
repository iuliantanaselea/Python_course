# METODE DE STRING
elf = "alpha 0123456789 ASD"

# len = metoda de string
# len = se aplica datelor care au "lungime" ( daca este transformat in string)
#Lungimea string-ului
print(len(elf))

# REPLACE
# inlocuire caractere din vairabila existenta
druid = elf.replace("alpha", "beta")
print(f"druid = {druid}")
print(f"elf = {elf}")

# replace inlocuieste doar daca gaseste
druid2 = elf.replace ("ASD", "bon")
print (druid2)

# Printare de string partiala ( SLICING )
print(elf[:10]) # metoda de slicing - primele caractere. Asa pot printa sau accesa doar o parte din string
print(elf[-10:]) #metoda de slicing - ultimele caractere
print(elf[4:8]) #metoda de slicing - ce "zona anume"


# STRING-ul este un tip de data IMMUTABLE (nu pot sa schimb variabila respectiva)
print(elf[0])
print(elf[19])
# elf[0] = "X"
elf = "X" # a inlocuit ce scria anterior / suprascriere
print(elf)
# !!! 'str' object does not support item assignment

print("-" * 30) #separator pentru vizualizare in consola


#numar de aparitii a unui caracter - COUNT
elf = "alpha 0123456789 ASD"
print(elf.count("a")) # de cate ori apare caracterul "a" intr-un string (! CASE SENSITIVE)
print(elf.count("alpha1"))

print("-" * 30)

nume = "kogalniceanu"
print(nume.upper()) #transforma tot string-ul in litere mari
print(nume.capitalize()) #transforma prima litera in litera mare

print("-" * 30)

print(nume.find("ala")) # "-1" = nu a gasit sirul de caractere
print(nume.find("cea"))