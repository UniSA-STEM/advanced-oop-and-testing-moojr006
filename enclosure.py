'''
File: enclosure.py
Description: A brief description of this Python module.
Author: Jason Moore
ID: 110456746
Username: moojr006
This is my own work as defined by the University's Academic Integrity Policy.
'''
from animal import Animal

#Still need to add some validation for size & cleanliness level
class Enclosure:
    environments = ["Grassy", "Aviary", "Vivarium"]

    def __init__(self, name: str, size: int, environment_type: str):
        self.__name = name
        self.__size = size
        self.__cleanliness_level = 10
        self.__animals = []
        if environment_type not in Enclosure.environments:
            raise ValueError(f"You must enter one of the following environments: {Enclosure.environments}")
        else:
            self.__environment_type = environment_type


    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str):
        self.__name = name

    def get_size(self) -> int:
        return self.__size

    def set_size(self, size: int):
        self.__size = size

    def get_environment_type(self) -> str:
        return self.__environment_type

    def get_cleanliness_level(self) -> int:
        return self.__cleanliness_level

    def set_cleanliness_level(self, level: int):
        self.__cleanliness_level = level

    def get_animal(self):
        if len(self.__animals) == 0:
            return f"There is no animal inside the enclosure"
        else:
            return [animal for animal in self.__animals]

    def __add_animal(self, animal: Animal):
        if isinstance(animal, Animal):
            self.__animals.append(animal)
        else:
            raise TypeError("You must enter an animal object.")

    def add_animal(self, animal: Animal):
        return self.__add_animal(animal)

    def __remove_animal(self, animal: Animal):
        if isinstance(animal, Animal):
            self.__animals.remove(animal)
        else:
            raise TypeError("You must enter an animal object.")

    def __report_status(self):
        return f"{self.get_name()} cleanliness level is {self.get_cleanliness_level()}"

    def report_status(self):
        return self.__report_status()

    def __clean_enclosure(self):
        self.cleanliness_level = 10
        return f"{self.name} has been cleaned."

    def clean_enclosure(self):
        return self.__clean_enclosure()

    name = property(get_name, set_name)
    size = property(get_size, set_size)
    environment_type = property(get_environment_type)
    cleanliness_level = property(get_cleanliness_level, set_cleanliness_level)
    animal = property(get_animal)












