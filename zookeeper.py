'''
File: zookeeper.py
Description: A brief description of this Python module.
Author: Jason Moore
ID: 110456746
Username: moojr006
This is my own work as defined by the University's Academic Integrity Policy.
'''
#potential update to health record when noticing sick animals?
from staff import Staff
from enclosure import Enclosure
from animal import Animal

class ZooKeeper(Staff):
    def __init__(self, name, role):
        super().__init__(name, role)

    def perform_duties(self):
        for enclosure in self.enclosures:
            enclosure.clean_enclosure()
            print(f"{enclosure.name} has been cleaned.")
            for animal in enclosure.animal:
                if isinstance(animal, Animal) and animal in self.animals:
                    if animal.is_sick == True:
                        animal.health_record.record_entry(f"{animal.name} has had a routine health check.", "Low")
                        print(f"Unable to feed because {animal.name} is sick.")
                        animal.health_record.record_entry(f"{animal.name} is sick.", "High")
                    else:
                        animal.health_record.record_entry(f"{animal.name} has had a routine health check.", "Low")
                        animal.health_record.record_entry(f"{animal.name} is healthy.", "Low")
                        if animal.diet == "herbivore":
                            print(f"{animal.name} has been fed hay.")
                            if enclosure.cleanliness_level > 0:
                                enclosure.cleanliness_level -= 1
                            animal.health_record.record_entry(f"{animal.name} has been fed hay.", "Low")
                        elif animal.diet == "carnivore":
                            print(f"{animal.name} has been fed meat.")
                            if enclosure.cleanliness_level > 0:
                                enclosure.cleanliness_level -= 1
                            animal.health_record.record_entry(f"{animal.name} has been fed meat.", "Low")









