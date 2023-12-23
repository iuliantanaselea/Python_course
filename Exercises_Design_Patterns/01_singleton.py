"""
Singleton
Se da următoarea clasa:


class PresedinteRomania:

    def __str__(self):
        return "Eu sunt presedintele Romaniei"

    def say_hello(self):
        return f'Salut! {self}'

In momentul de fata, dacă încercăm să creăm mai multe obiecte din clasa aceasta, vom putea:

a = PresedinteRomania()
b = PresedinteRomania()

print(f'ID(a) = {id(a)}')
print(f'ID(b) = {id(b)}')
print(f'Acelasi obiect? {a is b}')

Scopul acestui exercițiu este sa modificăm clasa de mai sus folosind DP Singleton pentru a obține mereu același obiect:
Vom folosi functia `__new__` (adevăratul constructor din Python)
Vom tine singurul obiect pe clasa (cls), și îl vom crea doar la prima apelare a lui __new__
La orice alta apelare, vom returna obiectul deja existent
"""


class PresedinteRomania:
    _instance = None

    def __new__(cls):
        """
        Metoda speciala __new__ este responsabila pentru crearea instantei obiectului.
        In marjoritatea cazurilor nu este nevoie sa suprascriem aceasta metoda, dar pentru
        singleton acesta este locul in care ne asiguram ca exista doar o singura instanta
        """
        if cls._instance is None:
            cls._instance= super(PresedinteRomania, cls).__new__(cls)
            """
            Verificam daca esista deja o instanta. Daca nu, cream una noua.
            Metoda super() ofera o cale de a apela metode din clasa de baza (parinte).
            In acest caz --> obiect
            """
        return cls._instance

    def __str__(self):
        return "Eu sunt presedintele Romaniei"

    def say_hello(self):
        return f'Salut! {self}'

a = PresedinteRomania()
b = PresedinteRomania()

print(f'ID(a) = {id(a)}')
print(f'ID(b) = {id(b)}')
print(f'Acelasi obiect? {a is b}')


"""
Factory Pattern
Acest pattern ne permite sa creăm un obiect dintr-o clasa folosind o alta clasa (fabrica). Fabrica are posibilitatea de a crea obiecte din mai multe clase (de obicei aceste clase sunt siblings, adica mostenesc de la acelasi parinte).


Vom implementa următoarele clase:
English/French/Spanish Translator – clase care știu sa traduca cuvinte din română în limba specificata
translations va fi un dicționar cu acele cuvinte, exemplu `{ “masina”: “car” }` – se poate hardcoda în clasa
localize va fi o funcție care pentru un parametru de intrare, ne va da traducerea lui în acea limba (exemplu `input(“masina”)` returneaza “car”)

TranslatorFactory – clasa care are o singura metoda (preferabil statica sau de clasa) numita get_translator(language) – in functie de parametrul language, returnează un translator object.


factory = TranslatorFactory()

english_trans = factory.get_translator('en')
spanish_trans = factory.get_translator('es')

print(f'In engleza zicem {english_trans.localize("masina")}')
print(f'In spaniola zicem {spanish_trans.localize("masina")}')

"""


class Fabrica:
    def __init__(self, translations):
        self.translations = translations

    def localize(self, word):
        return self.translations.get(word, "Translation not available")


class EnglishTranslator(Fabrica):
    def __init__(self):
        super().__init__(
            {'masina': 'car',
             'barbat': 'man',
             'femeie': 'woman',
             'child': 'copil'
             })


class FrenchTranslator(Fabrica):
    def __init__(self):
        super().__init__(
            {'masina': 'voiture',
             'barbat': 'homme',
             'femeie': 'femme',
             'child': 'enfant'
             })


class SpanishTranslator(Fabrica):
    def __init__(self):
        super().__init__(
            {'masina': 'coche',
             'barbat': 'hombre',
             'femeie': 'mujer',
             'child': 'nino'
             })


class TranslatorFactory:
    @classmethod
    def get_translator(cls, language):
        if language == 'en':
            return EnglishTranslator()
        elif language == 'fr':
            return FrenchTranslator()
        elif language == 'es':
            return SpanishTranslator()
        else:
            return ValueError("Invalid language")


factory = TranslatorFactory()

english_trans = factory.get_translator('en')
french_trans = factory.get_translator('fr')
spanish_trans = factory.get_translator('es')

print(f'In engleza zicem {english_trans.localize("masina")}')
print(f'In spaniola zicem {spanish_trans.localize("masina")}')
print(f'In franceza zicem {french_trans.localize("masina")}')

print("-" * 40)

#Varianta 2 folosind abstractmethod

from abc import ABC, abstractmethod

class TranslatorInterface(ABC):
    @staticmethod
    @abstractmethod

    def localize(word):
        pass


class EnTranslator(TranslatorInterface):
    traduceri = {
        'masina': 'voiture',
        'barbat': 'homme',
        'femeie': 'femme',
        'child': 'enfant'
    }

    @staticmethod
    def localize(word):
        return EnTranslator.traduceri.get(word, word)  # prima- ce returneaza, a doua- ce returneaza daca nu exista cuvantul

class FrTranslator(TranslatorInterface):
    traduceri = {
        'masina': 'car',
        'barbat': 'man',
        'femeie': 'woman',
        'child': 'copil'
    }

    @staticmethod
    def localize(word):
        return FrTranslator.traduceri.get(word, word)  # prima- ce returneaza, a doua- ce returneaza daca nu exista cuvantul

class EsTranslator(TranslatorInterface):
    traduceri = {
        'masina': 'coche',
        'barbat': 'hombre',
        'femeie': 'mujer',
        'child': 'nino'
    }

    @staticmethod
    def localize(word):
        return EsTranslator.traduceri.get(word, word)  # prima- ce returneaza, a doua- ce returneaza daca nu exista cuvantul

print(f"In engleza zicem {EnTranslator.localize('masina')}")
print(f"In franceza zicem {FrTranslator.localize('masina')}")
print(f"In spaniola zicem {EsTranslator.localize('masina')}")