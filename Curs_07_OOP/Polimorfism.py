from abc import ABC, abstractmethod


class Buyable(ABC):
    @abstractmethod
    def label(self):
        pass


class Product(Buyable):
    def __init__(self, price, name):
        self.price = price
        self.name = name

    def label(self):
        print(f"Eu sunt {self.__class__.__name__}: {self.name}")


class BioProduct(Product):
    def __init__(self, price, name, source):
        super().__init__(price, name)
        self.source = source


class RawProduct(Product):
    def __init__(self, price, name, time_on_shelf):
        super().__init__(price, name)
        self.time_on_shelf = time_on_shelf

def see_product_labels(products):
    for product in products:
        product.label()


ps = [
    Product(10, "Branza de vaca"),
    BioProduct(15.66, "Branza de vaca", "La bunici"),
    Product(9.67, "Oua"),
    BioProduct(17.54, "Oua", "La bunici"),
    RawProduct(4.99, "Mere", 2),
    BioProduct(3.88, "Mere", "La bunici"),
    Product(45.99, "Detergent rufe"),
    BioProduct(67.99, "Detergent rufe", "Lab Detergent Bio"),
    RawProduct(13.89, "Struguri", 1)
]
see_product_labels(ps)

"""
Polimorfismul este conceptul de a furniza o singura interfata catre diferite tipuri de obiecte.
In exemplul de mai sus apare ideea de subtipare prin care in momentul in care codul este
rulat isi va da seama din ce clasa este apelata functia label pentru a afisa numele clasei
corespunzator.
"""