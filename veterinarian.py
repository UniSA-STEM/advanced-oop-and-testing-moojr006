'''
File: veterinarian.py
Description: A brief description of this Python module.
Author: Jason Moore
ID: 110456746
Username: moojr006
This is my own work as defined by the University's Academic Integrity Policy.
'''
from staff import Staff


class Veterinarian(Staff):
    def __init__(self, name, role):
        """Instantiate Veterinarian with name and role"""
        super().__init__(name, role)

    def perform_duties(self):
        """Perform routine Veterinarian duties.

        Checks each animal if they are assigned Veterinarian care:
            - Treat animal if identified as sick.
            - Update animal health record with all treatment steps.
            - Updates animal is_sick boolean.
        """
        for animal in self.animals:
            if animal.is_sick == True:
                print(f"{animal.name} has been taken in for treatment.")
                animal.health_record.record_entry(f"{animal.name} has been taken in for treatment.", "High")
                animal.is_sick = False
                print(f"{animal.name} is no longer sick.")
                animal.health_record.record_entry(f"{animal.name} is no longer sick.", "Medium")


