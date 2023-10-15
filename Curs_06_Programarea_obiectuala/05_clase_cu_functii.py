class Dog:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def bark(self):  # self --> referinta catre obiectul curent(trebuie sa apara mereu, primul)
        print("Woof")

    def get_name(self):
        return f"Eu sunt {self.name}"

d = Dog(age=5, name="Mirel")
d.bark()

print(d.get_name())

