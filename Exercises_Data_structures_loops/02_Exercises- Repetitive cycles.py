#Exercitiul 1
"""
1.Având lista:
mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']

Folosește un for că să iterezi prin toată lista și să afișezi;
‘Mașina mea preferată este x’.
Fă același lucru cu un for each.
Fă același lucru cu un while.
"""
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']

#for loop
for masina in masini:
    print(f"Masina mea preferata este {masina}")

print('-'*30)
#while loop
i=0
while i<len(masini):
    print(f"Masina mea preferata este {masini[i]}")
    i+= 1

#Exercitiul 2
"""
2. Aceeași listă:
Folosește un for else
În for
Modifică elementele din listă astfel încât să fie scrise cu majuscule, exceptând primul și ultimul.
În else:
  Printează lista.
"""
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']

for index, masina in enumerate(masini): #utilizam functia enumerate pentru a obtine indexul fiecarui element din lista impreuna cu valoarea acestuia
    if index == 0 or index == len(masini)-1: #primul si ultimul elem din lista nu va fi upper
        continue
    masini[index]=masina.upper() #MODIFICA CARACTERELE LISTEI IN UPPER
    # print(enumerate(masini))
else:
    print(masini)

#Exercitiul 3
"""3. Aceeași listă:
Vine un cumpărător care dorește să cumpere un Mercedes.
Iterează prin ea prin modalitatea aleasă de tine.
Dacă mașina e mercedes:
   Printează ‘am găsit mașina dorită de dvs’
   Ieși din ciclu folosind un cuvânt cheie care face acest lucru
Altfel:
   Printează ‘Am găsit mașina X. Mai căutam‘
"""
masini = ['Audi', 'Volvo', 'BMW', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
for masina in masini:
    if masina == 'Mercedes':
        print("Am gasit masina dorita de dvs")
        break
else:
    print("Nu am gasit masina. Mai cautam")
# TEMA CU WHILE

#Exercitiul 4
"""4. Aceeași listă;
Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu excepția Trabant și Lăstun. 

Dacă mașina e Trabant sau Lăstun:
   Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie else).
Printează S-ar putea să vă placă mașina x.
"""
masini = ['Audi', 'Volvo', 'BMW', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
for masina in masini:
    if masina == 'Trabant' or masina == "Lăstun":
        continue
    print(f"S-ar putea sa va placa masina {masina}")
#Exercitiul 5
"""
5. Modernizează parcul de mașini:

Crează o listă goală, masini_vechi.
Iterează prin mașini.
Când găsesti Lăstun sau Trabant:
Salvează aceste mașini în masini_vechi.
Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).
Printează Modele vechi: x.
Modele noi: x.
"""
masini_vechi=[]
masini = ['Audi', 'Volvo', 'BMW', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
for index, masina in enumerate(masini):
    if masina == "Lăstun" or masina == "Trabant":
        masini_vechi.append(masina)
        masini[index] = 'Tesla'
print(f"Modele vechi: {masini_vechi}")
print(f"Modele noi: {masini}")

#Exercitiul 6
"""6. Având dict:
pret_masini = {
    'Dacia': 6800,
    'Lăstun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}

Vine un client cu un buget de 15000 euro.

Prezintă doar mașinile care se încadrează în acest buget.
Iterează prin dict.items() și accesează mașina și prețul.
Printează Pentru un buget de sub 15000 euro puteți alege mașină xLastun
Iterează prin listă.
"""
pret_masini = {
    'Dacia': 6800,
    'Lăstun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}
for masina, pret in pret_masini.items():
    if pret < 15000:
        print(f"Pentru un buget de sub 15000 euro puteți alege mașina {masina}")

#Exercitiul 7
"""7. Având lista:
numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
Iterează prin ea.
Afișează de câte ori apare 3 (nu ai voie să folosești count).
"""
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
aparitii = 0
for numar in numere:
    if numar == 3:
        aparitii +=1
print(f"Numar aparitii cifra 3: {aparitii}")

#Exercitiul 8
"""
8. Aceeași listă:
Iterează prin ea
Calculează și afișează suma numerelor (nu ai voie să folosești sum).
"""
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
suma = 0
for numar in numere:
    suma += numar
print(f"Suma este: {suma}")

#Exercitiul 9
"""9. Aceeași listă:
Iterează prin ea.
Afișază cel mai mare număr (nu ai voie să folosești max).

"""
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
maxim = 0
for numar in numere:
    if maxim < numar:
        maxim = numar
print(f"Maxim: {maxim}")

#Exercitiul 10
"""
10. Aceeași listă:
Iterează prin ea.
Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă.
Ex: dacă e 3, să devină -3
Afișază noua listă.
"""
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
index = 0
for numar in numere:
    if numar > 0:
        numere[index] = numar* -1
        index+= 1
print(numere)

#Exercitiul 11
"""
11.
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
Itereaza prin listă alte_numere 
Populează corect celelalte liste
Afișează cele 4 liste la final
"""
# alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# numere_pare = []
# numere_impare = []
# numere_pozitive = []
# numere_negative = []
# for numar in alte_numere:
#     if numar % 2 == 0:
#         numere_pare.append(numar)
#     else:
#         numere_impare.append(numar)
#     if numar >0:
#         numere_pozitive.append(numar)
#     else:
#         numere_negative.append(numar)
#
# print(f"numere_pare: {numere_pare}")
# print(f"numere_impare: {numere_impare}")
# print(f"numere_pozitive: {numere_pozitive}")
# print(f"numere_negative: {numere_negative}")

"""
12. Aceeași listă:
Ordonează crescător lista fară să folosești sort.
Te poți inspira vizual de aici.
https://www.youtube.com/watch?v=lyZQPjUT5B4
"""

# alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
#
# sorted = False
# while not sorted:
#     sorted = True
#     for i in range(len(alte_numere)- 1):
#         if alte_numere[i] >alte_numere[i+1]:
#             alte_numere[i], alte_numere[i+1] = alte_numere[i+1], alte_numere[i]
#             sorted = False
# print(alte_numere)

"""
13. Ghicitoare de număr:
numar_secret = Generați un număr random între 1 și 30
Numar_ghicit = None
Folosind un while
   User alege un număr
   Programul îi spune:
Nr secret e mai mare
Nr secret e mai mic
Felicitări! Ai ghicit!
"""
#
# import _random
# nr_secret = int()

""""14. Alege un număr de la tastatură
Ex: 7
Scrie un program care să genereze în consolă următoarea piramidă
1
22
333
4444
55555
666666
7777777
"""
#
# numar= int(input("introdu nr:"))
# for i in range(1, numar+1):
#     linia = str(i) *i
#     print(linia)

"""

15.
tastatura_telefon = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  [0]
]
Iterează prin listă 2d
Printează ‘Cifra curentă este x’
(hint: nested for - adică for în for)
"""

# tastatura_telefon = [
#   [1, 2, 3],
#   [4, 5, 6],
#   [7, 8, 9],
#   [0]
# ]
#
# for row in tastatura_telefon:
#     for cifra in row:
#         print(f"cifra este {cifra}")
#
# lista_2d = [
#   [1, 2, 3],
#   [4, 5, 6],
#   [7, 8, 9],
#   [0]
# ]
#
# print(lista_2d[0]) #index de la lista mama
# print(lista_2d[2][1]) #primul index de la lista mama, al 2-lea index [1] din sublista

"""
Creati un program care are ca scop un meniu.
Meniul se va selecta prin introducerea de la tastaura a unui numar intre 1 si 5
captat intr-o variabila.
Prezentati prin afisare acest sir de caractere:
“””
1 – Afisare lista de cumparaturi
2 – Adaugare element
3 – Stergere element
4 – Sterere lista de cumparaturi
5 - Cautare in lista de cumparaturi
Q - Iesire din program
“””
Apoi folosindu-va de o constructie if-elif-else afisati:
- daca utilizatorul scrie de la tastaura 1 afisati “Afisare lista de cumparaturi”
- daca utilizatorul scrie de la tastaura 2 afisati “Adugare element”
- daca utilizatorul scrie de la tastaura 3 afisati “Stergere element”
- daca utilizatorul scrie de la tastaura 4 afisati “Sterere lista de cumparaturi”
- daca utilizatorul scrie de la tastaura 5 afisati “Adaugare element”
- daca utilizatorul scrie altceva de la tastaura afisati “Alegerea nu exista.
Reincercati”
- daca utilizatorul scrie de la tastaura Q afisati “Iesire din program”
"""
"""
Hint...
O sa lucrati cu:
- o lista
- While true
- if, elif, else
- break
- print
"""
print("-" * 30)
lista_cumparaturi = [apa,paine]
while True:
    # Solicităm utilizatorului să introducă o opțiune din meniu printr-un input.
    optiune = input("""
1 – Afisare lista de cumparaturi
2 – Adaugare element
3 – Stergere element
4 – Sterere lista de cumparaturi
5 - Cautare in lista de cumparaturi
Q - Iesire din program
    """)