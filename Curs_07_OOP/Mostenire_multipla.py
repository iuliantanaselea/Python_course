class Car:
    def go(self):
        print("Vrum vrum")

    def start(self):
        print("Starting car")


class Flyable:
    def fly(self):
        print("Flu flu")

    def start(self):
        print("Starting flyable")

class FlyingCar(Car,Flyable): #ordinea din paranteze stabileste o ordine de prioritate
    pass

fc = FlyingCar()
fc.fly()
fc.go()
fc.start()

#Method resolutin order (MRO) --> Regula dupa care se decide care este functia ce se apeleaza
# atunci cand avem o mostenire multipla de functii cu acelasi nume (de la stanga la dreapta)

class FlyingCar2(Flyable,Car):
    pass

fc2=FlyingCar2()
fc2.fly()
fc2.go()
fc2.start()