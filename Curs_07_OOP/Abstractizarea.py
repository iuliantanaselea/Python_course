# se defineste o clasa care nu poate exista de sine statatoare
# forteaza anumite comportamente pentru a putea defini clasa
#O clasa abstracta este o clasa care are cel putin o functie abstracta (fara implementare)
from abc import ABC, abstractmethod  # ABC = abstract base class


class Animal(ABC):  # clasele abstracte trebuie sa mosteneasca din ABC
    @abstractmethod
    def sound(self):
        pass  # functiile abstracte sunt functii fara implementare

    @abstractmethod
    def sleep(self):
        raise NotImplementedError


class Dog(Animal):
    def sound(self):
        print("Woof")

    def sleep(self):
        print("Zzzz")


class Cat(Animal):
    def sound(self):
        print("Miau")

    def sleep(self):
        print("Purr")
"""
a =Animal() --> Eroare pentru ca nu se pot instantia clase abstracte
a.sleep
"""

c = Cat()
c.sleep()
c.sound()