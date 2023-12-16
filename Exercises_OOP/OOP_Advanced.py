"""

ABSTRACTION
Clasa abstractă FormaGeometrica
Conține un field PI=3.14
Conține o metodă abstractă aria (opțional)
Conține o metodă a clasei descrie() - aceasta printează pe ecran ‘Cel mai probabil am colturi’

"""

from abc import ABC, abstractmethod


class FormaGeoemtrica(ABC):
    PI = 3.14

    @abstractmethod
    def aria(self):
        pass

    @classmethod
    def descriere(cls):
        print("Cel mai probabil am colturi")


"""
INHERITANCE
Clasa Pătrat - moștenește FormaGeometrica
constructor pentru latură

ENCAPSULATION
latura este proprietate privată
Implementează getter, setter, deleter pentru latură
Implementează metoda cerută de interfață (opțional, doar dacă ai ales să implementezi metoda abstractă aria)

Clasa Cerc - moștenește FormaGeometrica
constructor pentru rază
raza este proprietate privată
Implementează getter, setter, deleter pentru rază
Implementează metoda cerută de interfață - în calcul folosește field PI mostenit din clasa părinte (opțional, doar dacă ai ales să implementezi metoda abstractă aria)

POLYMORPHISM 
Definește o nouă metodă descrie - printează ‘Eu nu am colturi’

Creează un obiect de tip Pătrat și joacă-te cu metodele lui
Creează un obiect de tip Cerc și joacă-te cu metodele lui
"""


class Patrat(FormaGeoemtrica):
    def __init__(self, latura):
        self.__latura = latura  # folosind __, latura devine proprietate privata

    def aria(self):
        return self.__latura * self.__latura

    @property  # transforma metoda intr-o proprietate, si permite sa o accesezi ca pe o variabila
    def latura(self):
        return self.__latura

    @latura.getter
    def latura(self):
        print(f"Getter: Latura este {self.__latura}")
        return self.__latura

    @latura.setter
    def latura(self, latura):
        print(f"Setter: Noua latura este {latura}")
        self.__latura = latura

    @latura.deleter
    def latura(self):
        print(f"Deleter: Am sters latura")
        self.__latura = None


patrat1 = Patrat(20)
patrat1.descriere()
print(f"Latura este: {patrat1.latura}")
print(f"Aria este: {patrat1.aria()}")
patrat1.latura = 30
del patrat1.latura


class Cerc(FormaGeoemtrica):
    def __init__(self, raza):
        self.__raza = raza  # raza este proprietate privata

    @property
    def raza(self):
        return self.__raza

    @raza.getter
    def raza(self):
        print(f"Getter: Raza este {self.__raza} ")
        return self.__raza

    @raza.setter
    def raza(self, raza):
        print(f"Setter: Noua raza este {raza} ")
        self.__raza = raza

    @raza.deleter
    def raza(self):
        print(f"Deleter:Raza a fost stearsa")
        self.__raza = None

    def aria(self):
        aria_cercului = self.PI * self.__raza * self.__raza
        return aria_cercului

    def descriere(cls):
        print("Eu nu am colturi")


print("*" * 30)
cerc = Cerc(10)
cerc.descriere()
print(f"Raza este: {cerc.raza}")
print(f"Aria este: {cerc.aria()}")
cerc.raza = 20
del cerc.raza
