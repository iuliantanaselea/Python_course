class Dog:

    def __init__(self, age, name):
        self.age = age
        self.name = name

        # Magic methods / Dunder methods

    def __str__(self):
        # --> se va apela de fiecare data cand se printeaza un obiect de tipul Dog
        # sau se apeleaza functia str
        return f"Age: {self.age}, Name: {self.name}"

    def __repr__(self):
        return str(self) #sau return self.__str__()

    def __eq__(self, other): #comparatia se face self == other
        if not isinstance(other, Dog): #verificam daca obiectul other apartine clasei Dog
            return False
        return self.age == other.age and self.name == other.name


d = Dog(age=4, name='Rex')
d2 = Dog(age=14, name='Bruno')
print(d)
print(d2)

print('*' * 30)
t = str(d)  # aici se apeleaza tot functia __str__ din clasa Dog
print(t)

#--------------------------------

l = [d,d2] #lista contine obiecte de tip Dog
print (l) #lista contine referinte catre obiectele de tipul Dog,
# asa ca nu apeleaza functia __str_ ci apeleaza functia __repr__

#--------------------------------

d3= Dog(1,"Pufi")
d4= Dog(1,"Pufi")

print(d3==d4)
print(d3 == 5)