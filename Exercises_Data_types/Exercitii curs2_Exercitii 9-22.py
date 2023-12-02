"""
9. Citește o literă de la tastatură.
    Verifică și afișează dacă este vocală sau nu.
"""
#
# l=input("Introdu o litera:")
# if(l == "a" or l =='e' or l == 'i' or l == 'o' or l == 'u'):
#     print(f"Litera '{l}' este o vocala")
# else:
#     print(f"Litera '{l}' este o consoana")

"""
10.Transformă și printează notele din sistem românesc în  >
Peste 9 => A
Peste 8 => B
Peste 7 => C
Peste 6 => D
Peste 4 => E
4 sau sub => F

"""

# nota = float(input("Introdu o nota:"))
# if(nota > 9):
#     print("A")
# elif (nota > 8):
#     print("B")
# elif (nota > 7):
#     print("C")
# elif(nota > 6):
#     print("D")
# elif(nota > 4):
#     print("E")
# else:
#     print("F")
#

"""
11.Verifică dacă x are minim 4 cifre (x e int).
(ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)

"""
# x = int(input("Introdu un numar:"))
# if(x >= 1000):
#     print(f"Numarul {x} are minim 4 cifre")
# else:
#     print(f"Numarul {x} nu are minim 4 ciffe")

"""
12.Verifică dacă x are exact 6 cifre.
"""

# x = int(input("Introdu un numar:"))
# if (100000 <= x <= 999999):
#     print(f"Numarul {x} are 6 cifre")
# else:
#     print(f"Numarul {x} nu are 6 cifre")

"""
13.Verifică dacă x este număr par sau impar (x e int).
"""
# x = int(input("Introdu un numar:"))
# if(x % 2 == 0):
#     print(f"Numarul {x} este par")
# else:
#     print(f"Numarul {x} este impar")

"""
14.      x, y, z (int)
Afișează care este cel mai mare dintre ele?
"""
# x = int(input("x="))
# y = int(input("y="))
# z = int(input("z="))
#
# if (x > y and x > z):
#     print(f"{x} este cel mai mare numar")
# elif (y > x and y > z):
#     print(f"{y} este cel mai mare numar")
# elif (x == y == z):
#     print("Toate numerele sunt egale")
# else:
#     print(f"{z} este cel mai mare numar")

"""
15. X, y, z - reprezintă unghiurile unui triunghi
Verifică și afișează dacă triunghiul este valid sau nu.
"""
# x = float(input("x="))
# y = float(input("y="))
# z = float(input("z="))
# if x+y+z == 180:
#     print("Triunghiul este valid")
# else:
#     print("Triunghiul nu este valid")

"""
16. Având stringul: 'Coral is either the stupidest animal or the smartest rock'
Citește de la tastatură un int x
Afișează stringul fără ultimele x caractere
Exemplu: dacă ai ales 7 => 'Coral is either the stupidest animal or the smarte'
"""

# text = "Coral is either the stupidest animal or the smartest rock"
# lungime = len(text)
# x = int(input("x="))
# print(text[0:lungime-x])

#Varianta 2:
# text = 'Coral is either the stupidest animal or the smartest rock'  # Stringul inițial
# x = int(input("Introdu un număr întreg: "))  # Citirea numărului de la tastatură
#
# text_taiat = text[:-x]  # Obtinerea textului taiat fara ultimele x caractere
#
# print(text_taiat)  # Afisarea textului taiat

"""
17. Același string. Declară un string nou care să fie format din primele 5 caractere + ultimele 5.
"""
# text = "Coral is either the stupidest animal or the smartest rock"
# text_nou = text[:5] + text[-5:]
# print(text_nou)

"""
18. Același string. 
-Salvează într-o variabilă și afișează indexul de start al cuvântului rock (hint: este o funcție care te ajuta sa faci asta)
-Folosind această variabilă + slicing, afișează tot stringul până la acest cuvânt
-output: 'Coral is either the stupidest animal or the smartest' 
"""
# text = "Coral is either the stupidest animal or the smartest rock"
# index = text.index("rock")
# print(text[:index])

"""
19. Joc ghicit zarul
Caută pe net și vezi cum se generează un număr random
Ne imaginăm ca dai cu zarul și salvăm acest număr în dice_roll
Ia numărul ghicit de la utilizator
Verifică și afișează dacă utilizatorul a ghicit
Vei avea 3 opțiuni
Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y.
Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y.
Ai ghicit. Felicitări! Ai ales x si zarul a fost y.
"""
# import random
# x= random.randint(0,6)
# print(x)
# dice_roll = int(input("Da cu zarul:"))
# if(dice_roll < x):
#     print(f"Ai pierdut. Ai ales un numar mai mic. Ai ales {dice_roll} dar a fost {x}")
# elif (dice_roll > x):
#     print(f"Ai pierdut. Ai ales un numar mai mare. Ai ales {dice_roll} dar a fost {x}")
# else:
#     print(f"Felicitari! Ai ales {dice_roll} si zarul a fost {x}")


"""
20.  Citește de la tastatură un string
Verifică dacă primul și ultimul caracter sunt la fel. Se va folosi un assert
Atenție: se dorește ca programul să fie case insensitive - 'apA' e acceptat
"""

# text = str(input("Cuvantul este: "))
# text = text.lower()
# assert text[0] == text[-1]

"""
21. Având stringul '0123456789'
Afișează doar numerele pare 
Afișează doar numerele impare
(hint: folosește slicing, controlează din pas)
"""

# sir = '0123456789'
# lungime = len(sir)
# print(f"Numere pare: {sir[0:lungime:2]}")
# print(f"Numere impare: {sir[1:lungime:2]}")

#Varianta simplificata:
# text = '0123456789'
# numere_pare = text[::2] # Daca le lasi necompletate, startul si stop-ul sunt inceputul si sfarsitul
# print(numere_pare)
# numere_pas3 = text[::3] # De la inceput la sfarsit, cu pas 3
# print(f"Numere cu pas 3: {numere_pas3}")
# numere_impare = text[1:7:2] #Index start: 1, Index stop: 7, pas: 2
# print(numere_impare)
