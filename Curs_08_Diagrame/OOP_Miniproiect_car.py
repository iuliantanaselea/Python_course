"""
Mașină
Atribute: marca, model, viteza maximă, viteza_actuală, culoare, culori disponibile (set), înmatriculată (bool)
   Culoare = gri - toate mașinile când ies din fabrică sunt gri
   Viteza_actuală = 0 - toate mașinile stau pe loc când ies din fabrică
   Culori disponibile = alege tu 5-7 culori
   Marca = alege tu - fabrica produce o singură marcă, dar mai multe modele
   Înmatriculată = False
Constructor: model, viteza_maxima
Metode:
    *descrie() - se vor printa toate atributele, în afară de culori_disponibile
    *înmatriculare() - va schimba atributul înmatriculată în True
    *vopsește(culoare) - se va vopsi mașina în noua culoare DOAR dacă noua culoare e în opțiunea de culori disponibile, altfel afișați o eroare
    *accelerează(viteza) - se va accelera la o anumită viteză, dacă viteza e negativă-eroare, dacă viteza e mai mare decât viteza_max - masina va accelera până la viteza maximă
    *franeaza() - mașina se va opri și va avea viteza 0

"""


class Car:
    def __init__(self, model, viteza_maxima):
        self.model = model
        self.viteza_maxima = viteza_maxima

    marca = "Dacia"
    culoare = 'gri'
    viteza_actuala = 0
    culori_disponibile = ['rosie', 'verde', 'bleu', 'alb', 'gri']
    inmatriculata = False

    def descrie(self):
        print(
            f" Marca: {self.marca}, model: {self.model}, viteza_actuală: {self.viteza_actuala}, culoare: {self.culoare}, inmatriculata: {self.inmatriculata}")

    def inmatriculare(self):
        self.inmatriculata = True
        print("Masina a fost inmatriculata")

    def vopseste(self, culoare_noua):
        if self.culoare in self.culori_disponibile:
            self.culoare = culoare_noua
            print(f"Noua culoare este : {culoare_noua}")
        else:
            raise Exception("Culoarea aleasa nu este in lista")

    def accelereaza(self, viteza):
        if viteza < 0:
            raise Exception("Nu se poate accelera cu viteza negativa")
        elif viteza > self.viteza_maxima:
            self.viteza_actuala = self.viteza_maxima
        else:
            self.viteza_actuala = viteza
        print(f"Viteza actuala dupa accelerare este: {self.viteza_actuala}")

    def franeaza(self):
        self.viteza_actuala = 0
        print(f"Masina a franat. Viteza actuala este {self.viteza_actuala}")


car1 = Car('Sandero', 160)
car1.descrie()
car1.inmatriculare()
car1.vopseste('rosu')
car1.descrie()
car1.accelereaza(120)
car1.franeaza()