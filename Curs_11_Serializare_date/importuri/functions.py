from dataclasses import dataclass


@dataclass
class Car:
    model: str
    color: str


def print_name(name):
    print(f"Hi, {name}")


def get_last(numbers):
    if numbers:
        return numbers[-1]
