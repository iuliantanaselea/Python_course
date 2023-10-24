"""
Proxy este un sablon structural care lasa sa dai un substitut pentru un alt obiect.
Un obiect proxy controleaza accesul catre obiectul original lansand doar anumite operatii sa fie
    efectuate sau sa adauge pasi extra inainte sau dupa operatia in sine

Avantaje: - Poti controla obiectul real fara ca cei care il utilizeaza sa stie
          - Poti controla ciclul de viata al obiectului real cand celor care il utilizeaza nu le pasa despre asta
          - Obiectul Proxy functioneaza chiar daca obiectul real nu este pregatit sau nu este disponibil.
                Ex: putem folosi obiectul proxy pt a da mesaje ca serviciul nu este momentan disponibil

Dezavantaje: - codul devine mai complicat deoarece este necesara introducerea mai multor clase
             - rezultatul obtinut de la obiectul real poate fi intarziat, neavand acces direct la acesta
"""

from abc import ABC, abstractmethod


class Subject(ABC):
    @abstractmethod
    def request(self):
        pass


class RealSubject(Subject):
    def request(self):
        print("Real Subject: Handling request")


class Proxy(Subject):
    def __init__(self, real_subject):
        self.real_subject = real_subject

    def check_access(self):
        print("Proxy: Checking access before real request")
        return True

    def request(self):
        if self.check_access():
            self.real_subject.request()


rs = RealSubject()
p = Proxy(rs)
p.request()
