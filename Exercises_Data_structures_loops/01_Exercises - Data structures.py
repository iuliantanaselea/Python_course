"""
 Partea 1 - Structuri de date

Exerciții - studiu în workshopul de weekend

Pentru toate exercițiile se va folosi noțiunea de if în rezolvare.
Indirect vei exersa și operatorii în cadrul condițiilor ramurilor din if.
X poate fi inițializat direct în cod sau citit de la tastatură, după preferințe.
X este un int.
"""
# Exercitiul 1
"""
1. Declară o listă note_muzicale în care să pui do re mi etc până la do
Afișeaz-o.
Inversează ordinea folosind slicing și suprascrie această listă.
Printează varianta actuală (inversată).
Pe această listă aplică o metodă care bănuiești că face același lucru, adică să îi inverseze ordinea. Nu trebuie să o suprascrii în acest caz, deoarece metoda face asta automat.
Printează varianta actuală a listei. Practic ai ajuns înapoi la varianta inițială.
"""
"""
#lista initiala
note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
print(note_muzicale)
#inversare prin slicing
note_muzicale = note_muzicale[::-1]
print(f"lista inversata {note_muzicale}")
note_muzicale.reverse()
print(f"lista intiiala {note_muzicale}")
"""


#Exercitiul 2
"""
2. De câte ori apare ‘do’?
"""
"""
note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
nr_aparitii = note_muzicale.count('do')
print(f" 'do' apare de {nr_aparitii} ori")
"""

#Exercitiul 3
"""
3.Având 2 liste, [3, 1, 0, 2] și [6, 5, 4]
   Găsește 2 variante să le unești într-o singură listă. 
"""
lista1 = [3,1,0,2]
lista2 = [6,5,4]
#concatenare cu +
varianta1= lista1 + lista2
print(f"varianta 1: {varianta1}")
#varianta 2 cu extend
varianta2= lista1.copy()
varianta2.extend(lista2)
print(f"varianta 2: {varianta2}")

#Exercitiul 4
"""
4.
Sortează și afișează lista generată la exercițiul anterior.
Șterge numărul 0 folosind o funcție.
Afișaza iar lista.
"""
#sortare
varianta1.sort()
print("Lista sortata:", varianta1)

#stergere primul element din lista
varianta1.remove(0)
print("Lista - primul element: ", varianta1)

"""
5. Folosind un if verifică lista generată la exercițiul 3 și afișează:
Lista este goală.
Lista nu este goală.
"""

lista1=[3,1,0,2]
if len(lista1) == 0:
    print("Lista este goala")
else:
    print("Lista nu este goala")

"""
6. Folosește o funcție care să șteargă lista de la exercițiul 3.
"""

lista1.clear()

"""
7. Copy paste la exercițiul 5. Verifică încă o dată.
Acum ar trebui să se afișeze că lista e goală.
"""
if len(lista1) == 0:
    print("Lista este goala")
else:
    print("Lista nu este goala")

#Exercitiul 8
"""
8. Având dicționarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
Folosește o funcție că să afișezi Elevii (cheile)
"""
dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
for elev in dict1.keys():
    print(elev)

#Exercitiul 9
"""
9. Printează cei 3 elevi și notele lor
Ex: ‘Ana a luat nota {x}’
Doar nota o vei lua folosindu-te de cheie
"""
dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
# for elev, nota in dict1.items():
#     if type(nota)= 2:
#     print(f"{elev} a luat notele {nota}")
# else:
#     print(f"{elev} a luat notea {nota}")

#Exercitiul 10
"""
10. Dorel a făcut contestație și a primit 6
Modifică nota lui Dorel în 6
Printează nota după modificare
"""
dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
dict1['Dorel'] = 6
print("Dorel a luat nota", dict1['Dorel'])
print(dict1)

#Exercitiul 11
"""
11. Gigel se transferă din clasă
Căuta o funcție care să îl șteargă
Vine un coleg nou. Adaugă Ionică, cu nota 9
Printează noii elevi
"""
dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
#functia del - sterge element din dict
del dict1['Gigel']
## functia pop - sterge
dict1.pop('Ana')
#adaugare cheie si valoare
dict1['Ionica'] = 9
for elev in dict1.keys():
    print(elev)


#Exercitiul 12
"""
12. Ne imaginăm o echipă de fotbal pt teren sintetic.
3 Schimbări maxime admise:

Declară o Listă cu 5 jucători
Schimbari_efectuate = te joci tu cu valori diferite
Schimbari_max = 3
Dacă Jucătorul x e în teren și mai avem schimbări la dispoziție
Efectuează schimbarea 
Șterge jucătorul scos din listă
Adaugă jucătorul intrat
Afișază a intrat x, a ieșit y, mai ai z schimbări

Dacă jucătorul nu e în teren:
Afișază ‘nu se poate efectua schimbarea deoarece jucătorul x nu e în teren’
Afișază ‘mai ai z schimbări’

Testează codul cu diferite valori

Google search hint
“how to check if item is în list python”

"""
print('-'*30)
#Declara o lista cu 5 jucatori
# jucatori= ['j1', 'j2', 'j3', 'j4', 'j5']
# schimbari_efectuate = 0
# schimbari_max = 3
#
# jucatori_teren = 'j6'
# if jucatori_teren in jucatori:
#     jucator_iesit = jucatori_teren
#     jucator_intrat = 'jNou'
#     jucatori.remove(jucator_iesit)
#     jucatori.append(jucator_intrat)
#     schimbari_efectuate += 1
#     print(f"A intrat {jucator_intrat}, a iesit {jucator_iesit}, mai ai {schimbari_max-schimbari_efectuate} schimbari disponibile")
# else:
#     print(f"nu se poate efectua schimbarea deoarece jucătorul {jucator_iesit} nu e în teren")
#     print(f"mai ai {schimbari_max-schimbari_efectuate} schimbari")

"""
13.
Set
zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
Adaugă în zilele_sapt ‘luni’
Afișează zile_sapt
"""
zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
zile_sapt.add('luni')
print(zile_sapt)

"""
14.Folosește un if și verifică dacă:
Weekend este un subset al zilelor din săptămânii.
Weekend nu este un subset al zilelor din săptămânii.
"""
zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
if weekend.issubset(zile_sapt):
    print("Weekend este un subset al zilelor din săptămânii.")
else:
    print("Weekend nu este un subset al zilelor din săptămânii.")

"""
15. Afișează diferențele dintre aceste 2 seturi.
"""
diferenta = zile_sapt.difference(weekend) #face diferenta dintre seturi
print(f"Diferenta: {diferenta}")\

"""16. Afișează intersecția elementelor din aceste 2 seturi.
"""
intersectia = zile_sapt.intersection(weekend) #face intersectia de seturi
print(intersectia)

intersectia = zile_sapt & weekend #face intersectia de seturi
print(intersectia)
