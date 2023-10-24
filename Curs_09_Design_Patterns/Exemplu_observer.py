"""
Observer este un sablon de proiectare comportamental care te lasa sa definesti un mecanism de subscriere
prin care mai multe obiecte pot fi notificate despre evenimente care se intampla in
obiectele pe care le observa
"""

from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, observable):
        pass


class Observable(ABC):
    @abstractmethod
    def register_observer(self, observer):
        pass

    @abstractmethod
    def notify(self):
        pass


class Subject(Observable):
    _observers = []

    def __init__(self, message):
        self.__message = message

    def register_observer(self, observer):
        self._observers.append(observer)

    def notify(self):
        for ob in self._observers:
            ob.update(self)

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        self.__message = value
        self.notify()


class RealObserverA(Observer):
    def update(self, observable):
        if observable.message.startswith("a"):
            print("observer A notificat")


class RealObserverB(Observer):
    def update(self, observable):
        if observable.message.startswith("b"):
            print("observer B notificat")


a = RealObserverA()
b = RealObserverB()
sub = Subject("Salut")
sub.register_observer(a)
sub.register_observer(b)

print("--" * 30)
sub.message = "ana are mere"
print("--" * 30)
sub.message = "mesaj frumos"
print("--" * 30)
sub.message = "balaur"

print("--" * 30)

from dataclasses import dataclass


@dataclass
class Person(Observer):
    name: str

    def send_message(self, chat_room):
        message = input(f"{self.name} introdu un mesaj: ")
        chat_room.add_message(Message(self.name, message))

    def update(self, observable):
        if observable.istoric[-1].content.startswith(self.name):
            print(f"{self.name} ai primit un mesaj! ")
            response = input("Vrei sa raspunzi? (y/n)")
            if response == "y":
                self.send_message(observable)


@dataclass
class Message:
    author: str
    content: str


class ChatRoom(Observable):
    _observers = []

    def __init__(self):
        self.istoric = []

    def notify(self):
        for ob in self._observers:
            ob.update(self)

    def register_observer(self, observer):
        self._observers.append(observer)

    def add_message(self, message):
        self.istoric.append(message)
        self.notify()


chat = ChatRoom()
s = Person("Sergiu")
v = Person("Valentin")
c = Person("Carmen")
chat.register_observer(s)
chat.register_observer(v)
chat.register_observer(c)
s.send_message(chat)
