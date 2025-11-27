'''
File: bird.py
Description: Bird class that inherits from Animal class.
Author: Jason Moore
ID: 110456746
Username: moojr006
This is my own work as defined by the University's Academic Integrity Policy.
'''

from animal import Animal

class Bird(Animal):
    def __init__(self, name: str, age: int, diet: str) -> None:
        """Instantiate Bird with name, age, and diet."""
        super().__init__(name, age, diet)

    def make_sound(self):
        """Return Bird sound."""
        return f"{self.name} squawked!"