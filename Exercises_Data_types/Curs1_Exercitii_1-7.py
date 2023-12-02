"1.	În cadrul unui comentariu, explică cu cuvintele tale ce este o variabilă."

"""
O variabila este un container in care se stocheaza un anumit tip de date"""

"""
În limbajul de programare Python, o variabilă reprezintă o locație de memorie unde 
se pot stoca date. 
Aceasta acționează ca un container pentru a păstra informații temporare sau permanente,
 cum ar fi numere, 
texte, liste, obiecte sau alte tipuri de date.
"""

"""
2.	Declară și initializează câte o variabilă din fiecare din următoarele tipuri 
de variabilă:
•	string
•	int 
•	float
•	bool
"""
# Variabila de tip  string
nume = "Maria"
# Variabila de tip  int
varsta = 17
# Variabila de tip  float
inaltine = 1.79
# Variabila de tip  bool
este_minora = True

"""
3.	Utilizează funcția type pentru a verifica dacă au tipul de date așteptat.
"""
# Variabila de tip  string
nume = "Maria"
print(type(nume))
# Variabila de tip  int
varsta = 17
print(type(varsta))
# Variabila de tip  float
inaltine = 1.79
print(type(inaltine))
# Variabila de tip  bool
este_minora = True
print(type(este_minora))

"""
4.	Rotunjește ‘float’-ul folosind funcția round() și salvează această modificare în 
aceeași variabilă 
(suprascriere): Verifică tipul acesteia.
"""

#Variabila de tip float
inaltime = 1.79
print("Tipul variabilei 'inaltime este,'" , type(inaltime))

#rotunjim valoarea

inaltime = round(inaltime)
print("Tipul variabilei 'inaltime este,'" , type(inaltime))

"""
5: Folosește print() și printează în consolă 4 propoziții folosind cele 4 variabile. 
Rezolvă nepotrivirile de tip prin ce modalitate dorești.
"""
print("#"*40)

nume = "Maria"
print(nume + " este colega mea")
print("Eu am " + str(varsta) + " ani")
print("Am " + str(inaltime) + " metri inaltime")
print("Eu sunt / si este " +str(este_minora) + " ca sunt minor a")

"""
6.	Citește de la tastatură:
•	numele;
•	prenumele.
    Afișează: 'Numele complet are x caractere'.
"""
print("#"*40)
"""
"""
"""# Sa ticitm numele si prenumele de la tastatura
nume = input("Introdu numele ...")
prenume = input("Introu prenumele...")

#Calculam numarul total de caractere din nume si prenume
nume_complet = nume + " " + prenume
lungimea_numelui = len(nume_complet)


#afisarea rezultatului
print("Numele complet are ", lungimea_numelui, "caractere.M")
"""
print("#"*40)
"""
Citește de la tastatură:
•	lungimea;
•	lățimea.
   Afișează: 'Aria dreptunghiului este x'.
"""

# citim lungimea si latimea
lungime = int(input("Introdu lunigmea dreptunghiului..."))
latimea = float(input("Introdu latimea dreptunghiului..."))

#aria dreptunghiului
aria = lungime * latimea

# Afisam rezultatul
print("Aria dreptunghoului este de... ", aria)