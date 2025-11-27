'''
File: zookeeper.py
Description: ZooKeeper class that performs common duties.
Author: Jason Moore
ID: 110456746
Username: moojr006
This is my own work as defined by the University's Academic Integrity Policy.
'''
from staff import Staff
from animal import Animal

class ZooKeeper(Staff):
    def __init__(self, name, role):
        """Instantiate ZooKeeper with name and role"""
        super().__init__(name, role)

    def perform_duties(self):
        """Perform routine ZooKeeper duties.

        Checks each animal if they are assigned to the ZooKeeper and
        enclosure:
            - Clean the enclosure
            - If an animal is_sick updated health record and it will not be fed
            - If an animal is not sick update health record
            - Feed the animal in accordance with its diet:
                - Herbivores eat hay
                - Carnivores eat meat
            - Reduces cleanliness level if animal has been fed
            - Update health record to show animal has eaten
        """
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
                            print(animal.eat())
                            if enclosure.cleanliness_level > 0:
                                enclosure.cleanliness_level -= 1
                            animal.health_record.record_entry(f"{animal.name} has been fed hay.", "Low")
                        elif animal.diet == "carnivore":
                            print(f"{animal.name} has been fed meat.")
                            print(animal.eat())
                            if enclosure.cleanliness_level > 0:
                                enclosure.cleanliness_level -= 1
                            animal.health_record.record_entry(f"{animal.name} has been fed meat.", "Low")









