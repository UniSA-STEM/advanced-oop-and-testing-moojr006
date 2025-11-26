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
        """Instantiate Staff with name and role
        
        Initialise:
            __animals: Create an empty list which is an attribute to Staff
            __enclosures: Create an empty list which is an attribute to Staff
        """
        self.__name = name
        self.__role = role
        self.__animals = []
        self.__enclosures = []

    def get_name(self) -> str:
        """Returns Staff name."""
        return self.__name

    def set_name(self, name: str):
        """Set Staff name attribute"""
        self.__name = name

    def get_role(self) -> str:
        """Returns Staff role"""
        return self.__role

    def set_role(self, role: str):
        """Set Staff role attribute"""
        self.__role = role

    def get_animals(self) -> list:
        """Return a list of animals in Staff's care"""
        return [animal for animal in self.__animals]

    def get_enclosures(self) -> list:
        """Return a list on enclosures in Staff's care"""
        return [enclosure for enclosure in self.__enclosures]

    def __add_animal(self, animal: Animal):
        """Add an animal into Staff's care.

        Args:
            animal: Animal is a child Animal object either Mammal, Bird, or Reptile.

        Returns:
            str: Confirmation message if animal added or why it has not been added.
        """
        if animal in self.__animals:
            return f"{animal} is already being looked after by this keeper."
        else:
            try:
                if isinstance(animal, Animal):
                    self.__animals.append(animal)
                    return f"{animal.name} has been added to {self.name}'s responsibility"
                else:
                    raise TypeError(f"{animal} must be in Animal class")
            except TypeError as e:
                print(f"TypeError: {e}. Received {animal} instead.")

    def add_animal(self, animal: Animal):
        """Wrapper method for __add_animal"""
        return self.__add_animal(animal)

    def __remove_animal(self, animal: Animal):
        """Remove an animal into Staff's care.

                Args:
                    animal: Animal is a child Animal object either Mammal, Bird, or Reptile.

                Returns:
                    str: Confirmation message if animal removed or why it has not been removed.
        """
        try:
            if not isinstance(animal, Animal):
                raise TypeError(f"{animal} is not an animal.")
            else:
                if animal in self.__animals:
                    self.__animals.remove(animal)
                    return f"{animal.name} has been removed from {self.name}'s responsibility"
                else:
                    return f"{animal.name} is not being cared for by this keeper."
        except TypeError as e:
            print(f"Type Error: {e}. Received {animal} instead.")

    def remove_animal(self, animal: Animal):
        """Wrapper method for __remove_animal"""
        return self.__remove_animal(animal)

    def __add_enclosure(self, enclosure: Enclosure):
        """Add an enclosure into Staff's care.

            Args:
                enclosure: Enclosure object to be added into Staff care

            Returns:
                str: Confirmation message if enclosure added or why it has not been added.
        """
        try:
            if isinstance(enclosure, Enclosure):
                if enclosure not in self.__enclosures:
                    self.__enclosures.append(enclosure)
                    return f"{enclosure.name} has been added to {self.name}'s responsibility"
                else:
                    return f"{self.name} is already assigned to {enclosure.name}"
            else:
                raise TypeError("Enclosure must be an instance of Enclosure class.")
        except TypeError as e:
            print(f"TypeError: {e}. Received {enclosure}")

    def add_enclosure(self, enclosure: Enclosure):
        """Wrapper method for __add_enclosure"""
        return self.__add_enclosure(enclosure)

    def __remove_enclosure(self, enclosure: Enclosure):
        """Remove an enclosure into Staff's care.

                    Args:
                        enclosure: Enclosure object to be removed from Staff care

                    Returns:
                        str: Confirmation message if enclosure removed or why it has not been removed.
                """
        try:
            if isinstance(enclosure, Enclosure) and enclosure in self.__enclosures:
                self.__enclosures.remove(enclosure)
                return f"{enclosure.name} has been removed from {self.name}'s responsibility"
            else:
                raise Exception(f"Unable to perform action")
        except Exception as e:
            print(f"Error: {e}. Received {enclosure}.")

    def remove_enclosure(self, enclosure: Enclosure):
        """Wrapper method for __remove_enclosure."""
        return self.__remove_enclosure(enclosure)

    @abstractmethod
    def perform_duties(self):
        """Abstract method to be passed down to child classes."""
        pass

    name = property(get_name, set_name)
    role = property(get_role, set_role)
    animals = property(get_animals)
    enclosures = property(get_enclosures)








