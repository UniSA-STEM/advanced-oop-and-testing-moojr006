'''
File: enclosure.py
Description: Enclosure class that contains Animal & Staff objects.
Author: Jason Moore
ID: 110456746
Username: moojr006
This is my own work as defined by the University's Academic Integrity Policy.
'''
from animal import Animal
from mammal import Mammal
from bird import Bird
from reptile import Reptile


class Enclosure:
    environments = ["grassy", "aviary", "vivarium"]

    def __init__(self, name: str, size: int, environment_type: str):
        """Instantiate Enclosure with name, size and environment_type.

                Initialise:
                    __cleanliness_level: Integer that indicates cleanliness level
                    10 is the cleanest and 0 is the dirtiest
                    __animals: Create an empty list which is an attribute to Enclosure
                    __capacity: Minimum of 1 animal, for every 10 square metres (integer) added
                    an animal can be housed.

        Instantiation will raise ValueError if an incorrect environment type is given.
                """
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
        """Returns Enclosure name."""
        return self.__name

    def set_name(self, name: str):
        """Sets Enclosure name."""
        self.__name = name

    def get_size(self) -> int:
        """Returns Enclosure size."""
        return self.__size

    def set_size(self, size: int):
        """Sets Enclosure size."""
        self.__size = size

    def get_environment_type(self) -> str:
        """Returns Enclosure environment type."""
        return self.__environment_type

    def get_cleanliness_level(self) -> int:
        """Returns Enclosure cleanliness level."""
        return self.__cleanliness_level

    def set_cleanliness_level(self, level: int):
        """Sets Enclosure cleanliness level."""
        self.__cleanliness_level = level

    def get_animal(self):
        """Returns a list of animals within enclosure."""
        if len(self.__animals) == 0:
            return f"There is no animal inside the enclosure"
        else:
            return [animal for animal in self.__animals]

    def __add_animal(self, animal: Animal):
        """Adds animal to the Enclosure if it is not at capacity and is the
        correct environment type.

        Args:
            animal: Animal object to add to the Enclosure

        Mammals can only be added to grassy environment.
        Reptiles can only be added to vivarium environment.
        Birds can only be added to aviary environment."""
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
        """Wrapper method for __add_animal."""
        return self.__add_animal(animal)

    def __remove_animal(self, animal: Animal):
        """Remove an animal from Enclosure.

            Args:
                animal: Animal is a child Animal object either Mammal, Bird, or Reptile.

            Returns:
                str: Confirmation message if animal removed or why it has not been removed.
        """
        try:
            if isinstance(animal, Animal):
                self.__animals.remove(animal)
                print(f"{animal} has been removed from {self.get_name()}.")
            else:
                raise TypeError("You must enter an animal object.")
        except TypeError as e:
            print(f"TypeError: {e}. Received {animal} instead.")

    def remove_animal(self, animal: Animal):
        """Wrapper metho for __remove_animal."""
        return self.__remove_animal(animal)

    def __report_status(self):
        """Returns the cleanliness level of the enclosure in a report format."""
        return f"{self.get_name()} cleanliness level is {self.get_cleanliness_level()}"

    def report_status(self):
        """Wrapper method for __report_status."""
        return self.__report_status()

    def __clean_enclosure(self):
        """Sets cleanliness level back to cleanest state of 10

        Returns:
            str: Indicating that Enclosure has been cleaned"""
        self.cleanliness_level = 10
        return f"{self.name} has been cleaned."

    def clean_enclosure(self):
        """Wrapper method for __clean_enclosure."""
        return self.__clean_enclosure()

    name = property(get_name, set_name)
    size = property(get_size, set_size)
    environment_type = property(get_environment_type)
    cleanliness_level = property(get_cleanliness_level, set_cleanliness_level)
    animal = property(get_animal)












