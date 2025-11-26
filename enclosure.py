'''
File: enclosure.py
Description: A brief description of this Python module.
Author: Jason Moore
ID: 110456746
Username: moojr006
This is my own work as defined by the University's Academic Integrity Policy.
'''
from animal import Animal
from mammal import Mammal
from bird import Bird
from reptile import Reptile

#Still need to add some validation for size & cleanliness level
class Enclosure:
    environments = ["grassy", "aviary", "vivarium"]

    def __init__(self, name: str, size: int, environment_type: str):
        self.__name = name
        self.__size = size
        self.__cleanliness_level = 10
        self.__animals = []
        self.__capacity = max(1, self.__size // 10)
        environment_type = environment_type.lower()
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
        if len(self.__animals) < self.__capacity:
            try:
                if isinstance(animal, Animal):
                        try:
                            if isinstance(animal, Mammal) and self.environment_type == "grassy":
                                self.__animals.append(animal)
                            elif isinstance(animal, Bird) and self.environment_type == "aviary":
                                self.__animals.append(animal)
                            elif isinstance(animal, Reptile) and self.environment_type == "vivarium":
                                self.__animals.append(animal)
                            else:
                                raise ValueError(f"{animal.name} must be put in either a grassy, aviary, or vivarium environment")
                        except ValueError as e:
                            print(f"ValueError: {e}. Received {animal} instead.")
                else:
                    raise TypeError("You must enter an animal object")
            except TypeError as e:
                print(f"TypeError: {e}. Received {animal} instead.")
        else:
            print(f"This enclosure is at capacity. Unable to add more animals.")

    def add_animal(self, animal: Animal):
        return self.__add_animal(animal)

    def __remove_animal(self, animal: Animal):
        try:
            if isinstance(animal, Animal):
                self.__animals.remove(animal)
            else:
                raise TypeError("You must enter an animal object.")
        except TypeError as e:
            print(f"TypeError: {e}. Received {animal} instead.")

    def remove_animal(self, animal: Animal):
        return self.__remove_animal(animal)

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












