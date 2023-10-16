"""
Incapsularea se refera la ascunderea detaliilor de implementare ale unei clase fata de alte clase
Exista 3 tipuri de metode si atribute:
    1. Public --> accesibile peste tot
    2. Protected --> accesibile doar in ierarhia de mostenire ( _atribut ) "_"
    3. Private --> accesibile doar in clasa ( __atribut) "__"
"""


class Car():
    def __init__(self, model):
        self.__model = model

    @property # setare ca proprietate a campului __model
    def model(self):
        print("Setare ca proprietate")
        return self.__model

    @model.setter  # schimbare valoare
    def model(self, value):
        if value.startswith('B'): #restrictionare asignare valori atributului __model
            print("Nu se pot adauga modele care incep cu litera B")
            return
        print("Schimbare valoare model")
        self.__model = value

    @model.getter  # preluare valoare
    def model(self):
        print("Returnare valoare")
        return self.__model

    @model.deleter #eliberarea din memorie a valorii din campul __model
    def model(self):
        print("Stergere valoare")
        self.__model = None

c = Car('Dacia')
print(c.model) #se apeleaza getterul

c.model = "Volvo" #se apeleaza setter-ul
print(c.model)

c.model = "BMV"
print(c.model)

del c.model #se apeleaza deleter-ul
print(c.model)