'''
O clasa parinte poate fi mostenita de oricate clase copil
Aceste clase copil vor avea acces la toate atributele si metodele clasei parinte

'''
class Person:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def print_name(self):
        print(f"My name is {self.name}")


class Student(Person):
    pass


p = Person(30, 'Tony')
p.print_name()

s = Student(40, 'Johny')
s.print_name()

# utila in refolosirea codului


print('*'*40)

class Angajat(Person):
    def __init__(self, age, name, workplace):
        super().__init__(age, name) #este direct o referinta catre clasa parinte
        self.workplace = workplace
    def print_work(self):
        print(f'I work at {self.workplace}')

a = Angajat(30, "Girtan", "Autodesk")
a.print_name()
a.print_work()