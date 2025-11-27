'''
File: mammal.py
Description: Mammal class that inherits from Animal class.
Author: Jason Moore
ID: 110456746
Username: moojr006
This is my own work as defined by the University's Academic Integrity Policy.
'''

from animal import Animal

class Mammal(Animal):
    def __init__(self, name: str, age: int, diet: str) -> None:
        """Instantiate Mammal with name, age, and diet."""
        super().__init__(name, age, diet)

    def make_sound(self):
        """Return Mammal sound."""
        return f"{self.name} growled!"
