'''
File: veterinarian.py
Description: A brief description of this Python module.
Author: Jason Moore
ID: 110456746
Username: moojr006
This is my own work as defined by the University's Academic Integrity Policy.
'''
from staff import Staff
from enclosure import Enclosure
from animal import Animal

class VeterinarianZooKeep(Staff):
    def __init__(self, name, role):
        super().__init__(name, role)

    def perform_duties(self):
        for animal in self.animals:
            if animal.is_sick == True:
                print(f"{animal.name} has been taken in for treatment.")
                animal.is_sick = False
                print(f"{animal.name} is no longer sick.")
                #health record update?

