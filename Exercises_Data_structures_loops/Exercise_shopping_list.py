
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
lista_cumparaturi = ['apa', 'paine']
while True:
    # Solicităm utilizatorului să introducă o opțiune din meniu printr-un input.
    optiune = input("""
1 – Afisare lista de cumparaturi
2 – Adaugare element
3 – Stergere element
4 – Sterere lista de cumparaturi
5 - Cautare in lista de cumparaturi
Q - Iesire din program
Selectati optiunea:     
    """)
    if optiune == '1':
        print(lista_cumparaturi)
    elif optiune == '2':
        lista_cumparaturi.append(input("Introduceti un produs:"))
        print(lista_cumparaturi)
    elif optiune == '3':
        elem_sters =input("Sterge produsul urmator:")
        lista_cumparaturi.remove(elem_sters)
        print(lista_cumparaturi)
    elif optiune == '4':
        lista_cumparaturi.clear()
        print(lista_cumparaturi)
    elif optiune == '5':
        elem_cautat = input("Introdu elementul cautat")
        if elem_cautat in lista_cumparaturi:
            print(f"elementul '{elem_cautat}' este in lista de cumparaturi")
        else:
            print(f"elementul '{elem_cautat}' nu este in lista de cumparaturi")
    elif optiune == 'Q':
        print("Iesire din lista")
        break
    else:
        print("Alegerea nu exista. Reincercati")