'''
File: reptile.py
Description: Reptile class that inherits from Animal class.
Author: Jason Moore
ID: 110456746
Username: moojr006
This is my own work as defined by the University's Academic Integrity Policy.
'''

from animal import Animal

class Reptile(Animal):
    def __init__(self, name: str, age: int, diet: str) -> None:
        """Instantiate Reptile with name, age, and diet."""
        super().__init__(name, age, diet)

    def make_sound(self):
        """Return Reptile sound."""
        return f"{self.name} hissed!"