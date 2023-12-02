"""
Avand stringul: "Coral is either the stupidest animal or the smartest rock':
- afiseaza de cate ori apare cuvantul 'the';
"""

text = "Coral is either the stupidest animal or the smartest rock"
cuvant_cautat = " the "

numarul_de_aparitii = text.lower().count(cuvant_cautat)

print("Cuvantul {} apare de {} ori in text.".format(cuvant_cautat, numarul_de_aparitii))
print(f"Cuvantul '{cuvant_cautat}' apare de {numarul_de_aparitii} ori in text")

print("_"*40)

"""
Foloseste un assert ca sa verifici daca acest string contine doar numere.
"""

text = "Coral is either the stupidest animal or the smartest rock"
assert text.isdigit() == False

"""
11 Exercitiu:
-citeste de la tastatura un string de dimensiune impara;
-afiseaza caracterul din mijloc

#trebuie sa citim un string de la tastatura
input_string = input("Introdu un string de dimensiune impara: ")

#Verificam daca lungimea stringului este impara
lungime =len(input_string)
if len(input_string) %2 !=0 :
    #Afisam  caracterul din mijloc
    mijloc = len(input_string)//2
    caracter_mijloc = input_string[mijloc]
    print("Caracterul din mijloc este:", caracter_mijloc)
else:
    print("Lungimea stringului este para")
"""

"""
Lista [0,1,2,3] - se pot modifica valorile din lista
Tuple (0,1,2,3) - valorile nu se pot modifica
Dictionar {key: valoare}

"""

"""
12. Folosind o singura linie de cod:
- citeste un string de la tastatura (ex: 'alabala portocala');
-salveaza fiecare cuvant intr-o variabila
-printeaza ambele variabile pentru verificare

cuvant1, cuvant2 = input("Introdu un string din doua cuvinte...").split()
print(cuvant1)
print(cuvant2)
"""

"""
13. Exercitiu:
- citeste un string de la tastatura ( ex: alabala protocala)
-salveaza primul caracter intr-o variabila - indiferent care este el, incearca cu 2 stringuri diferite
- capitalizeaza acest caracter peste tot, mai putin pentru primul si ultimul caracter => alAbAlA portocAla

"""

"""
input_string = input("Introdu un string: ")
def capitalized_string(input_string):
    #salvam primul caracter dintr-o variabila
    primul_caracter = input_string[0]
    print(primul_caracter)
    capitalized_string = primul_caracter + input_string[1:-1].capitalize() + input_string[-1]

    return capitalized_string

result= capitalized_string(input_string)
print(result)
"""

"""
14.Exercițiu:
citește un user de la tastatură;
citește o parolă;
afișează: 'Parola pt user x este ***** și are x caractere';
***** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie să afișeze corect.

eg: parola abc => ***
      parola abcd => ****

"""

#citire user si parola de la tastatura
user = input("Introdu un user: ")
parola = input("Introdu o parola: ")

#calcularea numarului de caractere din parola
lungime_parola = len(parola)

#construim stingul cu caracterele asterix in functie de lungimea parolei
caracter_asterix = '*' * lungime_parola
print(f"Parola pentru user-ul {user} este {caracter_asterix} si are {lungime_parola} caractere")
print("parola pentru user {} este {} si are {} caractere" .format(user, caracter_asterix, lungime_parola))