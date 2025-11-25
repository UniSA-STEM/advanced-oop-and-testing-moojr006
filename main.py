'''
File: main.py
Description: A brief description of this Python module.
Author: Jason Moore
ID: 110456746
Username: moojr006
This is my own work as defined by the University's Academic Integrity Policy.
'''
import animal
from animal import Animal
from mammal import Mammal
from bird import Bird
from reptile import Reptile
from enclosure import Enclosure
from healthrecord import HealthRecord
from staff import Staff
from zookeeper import ZooKeeper
from veterinarian import Veterinarian

lion_1 = Mammal("Leopold", 2, "carnivore")
lion_den = Enclosure("lion den", 30, "grassy")
bird_1 = Bird("Polly", 4, "carnivore")
bird_cage = Enclosure("Polly's home", 15, "aviary")
snake_1 = Reptile("Abasilisk", 15, "carnivore")
snake_house = Enclosure("Snake house", 5, "vivarium")
keeper_1 = ZooKeeper("Debra", "ZooKeeper")
vet_1 = Veterinarian("Dale", "Veterinarian")

def zoo_operation(animal, enclosure):
    enclosure.add_animal(animal)
    keeper_1.add_enclosure(enclosure)
    keeper_1.add_animal(animal)
    keeper_1.perform_duties()
    print(animal.health_record.report())
    animal.is_sick = True
    keeper_1.perform_duties()
    print(animal.health_record.report())
    vet_1.add_enclosure(enclosure)
    vet_1.add_animal(animal)
    vet_1.perform_duties()
    keeper_1.perform_duties()
    print(animal.health_record.report())
    print(animal.is_sick)
    enclosure.remove_animal(animal)
    keeper_1.remove_animal(animal)
    keeper_1.remove_enclosure(enclosure)
    vet_1.remove_animal(animal)
    vet_1.remove_enclosure(enclosure)


zoo_operation(lion_1, lion_den)
print("\n\n")
zoo_operation(bird_1, bird_cage)
print("\n\n")
zoo_operation(snake_1, snake_house)











