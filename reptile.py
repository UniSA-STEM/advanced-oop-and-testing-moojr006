'''
File: reptile.py
Description: A brief description of this Python module.
Author: Jason Moore
ID: 110456746
Username: moojr006
This is my own work as defined by the University's Academic Integrity Policy.
'''

from animal import Animal

class Reptile(Animal):
    def __init__(self, name: str, age: int, diet: str) -> None:
        super().__init__(name, age, diet)

    def make_sound(self):
        return f"{self.name} hissed!"