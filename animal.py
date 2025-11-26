'''
File: animal.py
Description: A brief description of this Python module.
Author: Jason Moore
ID: 110456746
Username: moojr006
This is my own work as defined by the University's Academic Integrity Policy.
'''

from abc import ABC, abstractmethod
from healthrecord import HealthRecord


class Animal(ABC):
    diet_options = ["herbivore", "carnivore"]

    def __init__(self, name: str, age: int, diet: str)-> None:
        self.__name = name
        self.__age = age
        diet = diet.lower()
        if diet not in self.diet_options:
            raise TypeError("Diet must be one of" + ", ".join(Animal.diet_options))
        else:
            self.__diet = diet
        self.__health_record = HealthRecord(self.__name)
        self.__is_sick = False

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str):
        try:
            if isinstance(name, str):
                self.__name = name
            else:
                raise TypeError("Name must be a string")
        except TypeError as e:
            print(f"Type error: {e}. Received {name} instead.")


    def get_age(self) -> int:
        return self.__age

    def set_age(self, age: int):
        try:
            if isinstance(age, int):
                self.__age = age
            else:
                raise TypeError("Age must be an integer")
        except TypeError as e:
            print(f"Type error: {e}. Received {age} instead.")


    def get_diet(self) -> str:
        return self.__diet

    def set_diet(self, diet: str):
        diet = diet.lower()
        try:
            if isinstance(diet, str) and diet in Animal.diet_options:
                self.__diet = diet
            else:
                raise Exception("Invalid input")
        except Exception as e:
             print(f"Error: {e}. Received {diet} instead.")

    def get_is_sick(self):
        return self.__is_sick

    def set_is_sick(self, boolean: bool):
        try:
            if isinstance(boolean, bool):
                self.__is_sick = boolean
            else:
                raise ValueError("Must be a boolean value")
        except ValueError as e:
            print(f"Type error: {e}. Received {boolean} instead.")

    def get_health_record(self) -> HealthRecord:
        return self.__health_record

    def __eat(self):
        return f"{self.__name} is eating."

    def eat(self):
        return self.__eat()

    def __sleep(self):
        return f"{self.__name} is sleeping."

    def sleep(self):
        return self.__sleep()

    @abstractmethod
    def make_sound(self):
        pass

    name = property(get_name, set_name)
    age = property(get_age, set_age)
    diet = property(get_diet, set_diet)
    is_sick = property(get_is_sick, set_is_sick)
    health_record = property(get_health_record)


