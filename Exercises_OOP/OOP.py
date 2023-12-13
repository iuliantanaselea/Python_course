"""
Partea 2- OOP _ Clase & Obiecte


1.Clasa Cerc
    Atribute: rază, culoare
    Constructor pentru ambele atribute
    Metode:
•	descrie_cerc() - va PRINTA culoarea și raza
•	aria() - va RETURNA aria
•	diametru()
•	circumferinta()
"""


class Cerc:
    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare

    def descriere_cerc(self):
        print(f"Cercul are raza {self.raza} si culoarea {self.culoare}")

    def aria(self):
        return 3.14 * self.raza ** 2

    def diametru(self):
        return 2 * self.raza

    def circumferinta(self):
        return 2 * 3.14 * self.raza


cerc1 = Cerc(5, 'Mov')
cerc1.descriere_cerc()
print(f"Aria cercului este {cerc1.aria()}")
print(f"Diametrul cercului este {cerc1.diametru()}")
print(f"Circumferinta cercului este {cerc1.circumferinta()}")

print("*" * 30)
"""
2. Clasa Dreptunghi
     Atribute: lungime, lățime, culoare
     Constructor pentru toate atributele
     Metode:
descrie()
aria()
perimetrul()
schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic. 
Ea va lua ca și parametru o nouă culoare și va suprascrie atributul self.culoare. 
Poți verifica schimbarea culorii prin apelarea metodei descrie().
"""


class Dreptunghi:
    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def descriere(self):
        print(f"Dreptunghiul are lungime=  {self.lungime}, latime = {self.latime}, culoare = {self.culoare}")

    def aria(self):
        return self.lungime * self.latime

    def perimetru(self):
        return 2 * (self.lungime + self.latime)

    def schimba_culoare(self, noua_culoare):
        self.culoare = noua_culoare
        print(f"Noua culoare a dreptunghiului este {noua_culoare}")


dreptunghi1 = Dreptunghi(5, 10, "Albastru")
dreptunghi1.descriere()
print(f"Aria dreptunghiului este {dreptunghi1.aria()}")
print(f"Perimetrul dreptunghiului este {dreptunghi1.perimetru()}")
dreptunghi1.schimba_culoare("Rosu")

"""
3. Clasa Angajat
     Atribute: nume, prenume, salariu
     Constructor pentru toate atributele
     Metode:
descrie()
nume_complet()
salariu_lunar()
salariu_anual()
marire_salariu(procent)
"""
print("*" * 30)


class Angajat:
    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def descriere(self):
        print(f"Angajatul {self.nume} {self.prenume} are salariul {self.salariu} lei")

    def nume_complet(self):
        return self.nume + " " + self.prenume

    def salariu_lunar(self):
        return self.salariu

    def salariu_anual(self):
        return self.salariu * 12

    def marire_salariu(self, procent):
        self.procent = procent
        return self.salariu + (self.salariu * procent) / 100


angajat1 = Angajat("Mihai", "Popa", 6500)
angajat1.descriere()
print(angajat1.nume_complet())
print(f"Salariul lunar este {angajat1.salariu_lunar()}")
print(f"Salariul anual este {angajat1.salariu_anual()}")
print(f"Noul salariu este {angajat1.marire_salariu(23)}")

print("*" * 30)

"""
4. Clasa Cont
   Atribute: iban, titular_cont, sold
   Constructor pentru toate atributele
   Metode:
afisare_sold() - Titularul x are în contul y suma de n lei
debitare_cont(suma)
creditare_cont(suma)
"""


class Cont:
    def __init__(self, iban, titular_cont, sold):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold

    def afisare_sold(self):
        print(f"Titularul {self.titular_cont} are in contul {self.iban} suma de {self.sold} lei")

    def debitare_cont(self, suma):
        if suma > self.sold:
            print("Fonduri insuficiente")
        else:
            self.sold -= suma
            print(f"S-a debitat suma de {suma} lei din contul {self.iban}. Noul sold este {self.sold}")

    def creditare_cont(self, suma):
        self.sold += suma
        print(f"S-a creditat suma de {suma} lei din contul {self.iban}. Noul sold este {self.sold}")


cont1 = Cont(165822548624, "Mihai Popa", 5426)
cont1.afisare_sold()
cont1.debitare_cont(4300)
cont1.creditare_cont(3424)

"""
 5. Clasa Factură
     Atribute: seria (va fi constantă, nu trebuie constructor, toate facturile vor avea aceeași serie), 
     număr, nume_produs, cantitate, pret_buc
     Constructor: toate atributele, fără serie
     Metode:
schimbă_cantitatea(cantitate)
schimbă_prețul(pret)
schimbă_nume_produs(nume)
generează_factura() - va printa tabelar dacă reușiți

Factura seria x număr y
Data: generează automat data de azi
Produs | cantitate | preț bucată | Total 
Telefon |      7       |       700       | 49000     
"""
print("*"*30)
from datetime import date
from tabulate import tabulate

class Factura:
    serie = "X"

    def __init__(self, numar, nume_produs, cantitate, pret_buc):
        self.numar = numar
        self.nume_produs = nume_produs
        self.cantitate = cantitate
        self.pret_buc = pret_buc

    def schimba_cantitatea(self, cantitate):
        self.cantitate = cantitate

    def schimba_pretul(self, pret):
        self.pret_buc = pret

    def schimba_nume_produs(self, nume):
        self.nume_produs = nume

    def genereaza_factura(self):
        data = date.today().strftime("%d.%m.%Y") #formula pt formatare zi,luna,an
        total = self.cantitate * self.pret_buc
        # print("Factura seria", Factura.serie, "numarul", self.numar)
        # print("Data:", data)
        # print("Produs \t|\tCantitate\t|\tPret bucata\t|\tTotal")
        # print(self.nume_produs, "\t|\t", self.cantitate, "\t\t|\t", self.pret_buc, "\t\t|\t", total)
        header = ["Produs", "Cantitate", "Pret bucata", "Total"]
        col_names = [ [self.nume_produs, self.cantitate, self.pret_buc, total]]
        print("Factura seria", Factura.serie, "numarul", self.numar)
        print("Data", data)
        print(tabulate(col_names, headers = header,tablefmt="grid"))


factura1=Factura("213", "bicarbonat de sodiu", 10, 5.2)
factura1.genereaza_factura()
factura1.schimba_cantitatea(34)
factura1.schimba_pretul(435.2)
factura1.schimba_nume_produs("calculator")
factura1.genereaza_factura()