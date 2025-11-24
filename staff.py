'''
File: staff.py
Description: A brief description of this Python module.
Author: Jason Moore
ID: 110456746
Username: moojr006
This is my own work as defined by the University's Academic Integrity Policy.
'''
from abc import ABC, abstractmethod

from animal import Animal
from enclosure import Enclosure


class Staff(ABC):
    def __init__(self, name: str, role: str):
        self.__name = name
        self.__role = role
        self.__animals = []
        self.__enclosures = []

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str):
        self.__name = name

    def get_role(self) -> str:
        return self.__role

    def set_role(self, role: str):
        self.__role = role

    def get_animals(self) -> list:
        return [animal for animal in self.__animals]

    def get_enclosures(self) -> list:
        return [enclosure for enclosure in self.__enclosures]

    def __add_animal(self, animal: Animal):
        if not isinstance(animal, Animal):
            raise TypeError(f"{animal} is not an animal.")
        if animal not in self.__animals:
            self.__animals.append(animal)
            return f"{animal.name} has been added to {self.name}'s responsibility"
        else:
            raise ValueError(f"{animal.name} is already being looked after by this keeper.")

    def add_animal(self, animal: Animal):
        return self.__add_animal(animal)

    def __remove_animal(self, animal: Animal):
        if not isinstance(animal, Animal):
            raise TypeError(f"{animal} is not an animal.")
        if animal in self.__animals:
            self.__animals.remove(animal)
            return f"{animal.name} has been removed from {self.name}'s responsibility"
        else:
            return f"{animal.name} is not being cared for by this keeper."


    def remove_animal(self, animal: Animal):
        return self.__remove_animal(animal)

    def __add_enclosure(self, enclosure: Enclosure):
        if isinstance(enclosure, Enclosure):
            if enclosure not in self.__enclosures:
                self.__enclosures.append(enclosure)
                return f"{enclosure.name} has been added to {self.name}'s responsibility"
            else:
                raise ValueError(f"{self.name} is already assigned to {enclosure.name}")
        else:
            raise TypeError("Enclosure must be an instance of Enclosure class.")

    def add_enclosure(self, enclosure: Enclosure):
        return self.__add_enclosure(enclosure)

    def __remove_enclosure(self, enclosure: Enclosure):
        if isinstance(enclosure, Enclosure):
            if enclosure in self.__enclosures:
                self.__enclosures.remove(enclosure)
                return f"{enclosure.name} has been removed from {self.name}'s responsibility"
            else:
                raise ValueError(f"{enclosure.name} is not assigned to {self.name}")
        else:
            raise TypeError("Enclosure must be an instance of Enclosure class.")

    def remove_enclosure(self, enclosure: Enclosure):
        return self.__remove_enclosure(enclosure)

    @abstractmethod
    def perform_duties(self):
        pass

    name = property(get_name, set_name)
    role = property(get_role, set_role)
    animals = property(get_animals)
    enclosures = property(get_enclosures)








