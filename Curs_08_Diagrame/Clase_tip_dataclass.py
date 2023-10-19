from dataclasses import dataclass
from typing import List  # typing defineste tipuri de date


@dataclass
class Person:
    name: str
    age: int


@dataclass
class Student(Person):
    university: str
    grades: List[float]


p = Person('Adrian', 37)
print(p)
s = Student('John', 23,"Ion Mincu",[9.5,6.5,8.4])
print(s)

# O clasa de tip dataclass defineste automat functiile:
# __init__,__repr__, __eq__
