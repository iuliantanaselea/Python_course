"""
Singleton --> Design pattern care ne permite sa avem o clasa care returneaza mereu aceiasi instanta unica
          --> De obicei se foloseste in situatii in care nu ne intereseaza obiectul in sine ci doar
              anumite functionalitati ale acestuia
Ex:

O conexiune la o baza de date si foarte multe requesturi de la utilizatori care vor sa faca cereri la
baza de date. Daca de fiecare data cand intra in aplicatie, creaza conexiune baza de date pt a obtine id-ul
de sesiune al userului, cauta toate comentariile, toate postarile, adauga postare noua, modifica, etc creaza
10 conexiuni unice la aceeasi baza de date intr-un singur request, dureaza enorm.
    In schimb daca ai mereu o conexiune deschisa si o folosesti de fiecare data cand ai nevoie sa folosesti acea
sesiune, iti returneaza obiectul care deja exista, castigi foarte mult timp si putere de procesare, avand
mereu o conexiune deschisa, nemaiformand una noua.


Avantaje: - Poti fi sigur ca o clasa Singleton are doar o singura instanta
          - Poti avea acces global catre aceasta instanta
          - Obiectul Singleton este initializat doar o singura data (Prima data cand este cerut)

Dezavantaje: - Poate masca un design defectuos, de exemplu atunci cand componentele unui sistem
               stiu prea multe unele despre celelalte

"""


class SingletonLogger:
    _instance = None

    # functia __init__ in python nu este un constructor traditional ci doar un initializator.
    # inainte de __init__ este apelata functia __new__ unde se creaza de fapt obiectul.

    def __new__(cls, *args, **kwargs):  # este o metoda de clasa, nu de instanta, self facea referinta la obiectul curent
        # Functia new nu are "self" ca prim argument pentru ca "self" nu exista inca la momentul
        # rularii. In schimb avem "cls" care este o referinta catre clasa curenta.
        if cls._instance is None:  # prima data cand este apelata SingletonLogger se creaza obiectul.
            print("Creating object")
            cls._instance = super().__new__(cls)  # creaza in acel camp instance obiectul SingletonLogger
        return cls._instance  # returnam acelasi obiect de fiecare data


# logger = SingletonLogger()
# logger2 = SingletonLogger()
# print(logger, logger2)
# print(logger is logger2)

print("-" * 30)


class SingletonFileLogger(SingletonLogger):  # mostenirea facuta in acest fel duce la problema
    # ca obiectul instantei Singleton poate fi de tipul SingletonLogger, nu SingletonFileLogger
    # daca el se creaza inainte. Ca si solutie vezi exemplul de mai jos cu SingletonLoggerMultiClass
    def __init__(self, file_name):
        self.file_name = file_name


sfl = SingletonFileLogger("Hello.exe")
sfl2 = SingletonFileLogger("Hello2.exe")
print(sfl, sfl2)
print(sfl.file_name, sfl2.file_name)

print("-" * 30)


class SingletonLoggerMultiClass:
    _instance = {}

    def __new__(cls, *args, **kwargs):
        if cls._instance.get(cls) is None: #verifica daca exista deja o instanta pentru clasa curenta.
            # daca nu exista, o creaza.
            cls._instance[cls] = super().__new__(cls)
        return cls._instance[cls]


class SingletonFileLogger2(SingletonLoggerMultiClass):
    def __init__(self, file_name):
        self.file_name = file_name
l = SingletonLoggerMultiClass()
l2 = SingletonLoggerMultiClass()
s = SingletonFileLogger2("Hello.exe")
s2 = SingletonFileLogger2("Hello2.exe")
print (l,l2,s,s2)

