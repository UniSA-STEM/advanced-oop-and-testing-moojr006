'''
File: test_main.py
Description: A brief description of this Python module.
Author: Jason Moore
ID: 110456746
Username: moojr006
This is my own work as defined by the University's Academic Integrity Policy.
'''
import pytest
from animal import Animal
from reptile import Reptile
from mammal import Mammal
from bird import Bird
from enclosure import Enclosure
from staff import Staff
from veterinarian import Veterinarian
from zookeeper import ZooKeeper
from healthrecord import HealthRecord

class TestAnimals:
    @pytest.fixture
    def mammal(self):
        return Mammal("leopold", 5, "carnivore")

    def test_mammal(self, mammal):
        assert mammal.name == "leopold"
        assert mammal.age == 5
        assert mammal.diet == "carnivore"

    @pytest.fixture
    def bird(self):
        return Bird("polly", 3, "carnivore")

    def test_bird(self, bird):
        assert bird.name == "polly"
        assert bird.age == 3
        assert bird.diet == "carnivore"


    @pytest.fixture
    def reptile(self):
        return Reptile("abasilisk", 2, "carnivore")

    def test_reptile(self, reptile):
        assert reptile.name == "abasilisk"
        assert reptile.age == 2
        assert reptile.diet == "carnivore"


class TestEnclosure:
    @pytest.fixture
    def enclosure(self):
        return Enclosure("lion_den", 30, "grassy")

    @pytest.fixture
    def lion(self):
        return Mammal("leopold", 5, "carnivore")

    @pytest.fixture
    def lion1(self):
        return Mammal("leo", 5, "carnivore")

    @pytest.fixture
    def lion2(self):
        return Mammal("leopoldo", 5, "carnivore")

    @pytest.fixture
    def lion3(self):
        return Mammal("leopoldio", 5, "carnivore")


    def test_enclosure(self, enclosure, lion):
        enclosure.add_animal(lion)
        assert enclosure.name == "lion_den"
        assert enclosure.animal[0].name == "leopold"
        enclosure.remove_animal(lion)
        assert enclosure.animal == "There is no animal inside the enclosure"

    def test_capacity(self, lion, lion1, lion2, lion3, enclosure):
        enclosure.add_animal(lion)
        assert len(enclosure.animal) == 1
        enclosure.add_animal(lion1)
        assert len(enclosure.animal) == 2
        enclosure.add_animal(lion2)
        assert len(enclosure.animal) == 3
        enclosure.add_animal(lion3)
        assert len(enclosure.animal) == 3



    def test_wrong_environment(self, enclosure):
        polly = Bird("polly", 3, "carnivore")
        enclosure.add_animal(polly)
        assert enclosure.animal == "There is no animal inside the enclosure"

class TestHealthRecord:
    @pytest.fixture
    def healthrecord(self):
        return HealthRecord("Leopold")

    def test_add_entry(self, healthrecord):
        healthrecord.record_entry("Testing", "low")
        assert healthrecord.name == "Leopold"
        assert healthrecord.records[0][0] == "Testing"
        assert healthrecord.records[0][1] == "low"
        assert len(healthrecord.records) == 1

    def test_incorrect_entry(self, healthrecord):
        healthrecord.record_entry("Blow out", "Catastrophic")
        assert len(healthrecord.records) == 0

class TestBehaviour:

    @pytest.fixture
    def bird(self):
        return Bird("polly", 3, "carnivore")

    @pytest.fixture
    def snake(self):
        return Reptile("abasilisk", 2, "carnivore")

    def test_make_sound(self, bird, snake):
        assert bird.make_sound() == f"{bird.name} squawked!"
        assert snake.make_sound() == f"{snake.name} hissed!"

    def test_sleep(self, bird, snake):
        assert bird.sleep() == f"{bird.name} is sleeping."
        assert snake.sleep() == f"{snake.name} is sleeping."

    def test_eat(self, bird, snake):
        assert bird.eat() == f"{bird.name} is eating."
        assert snake.eat() == f"{snake.name} is eating."

class TestStaff:

    @pytest.fixture
    def zookeeper(self):
        return ZooKeeper("Debra", "ZooKeeper")

    @pytest.fixture
    def vet(self):
        return Veterinarian("Dale", "Veterinarian")

    @pytest.fixture
    def bird(self):
        return Bird("polly", 3, "carnivore")

    @pytest.fixture
    def snake(self):
        return Reptile("abasilisk", 2, "carnivore")

    @pytest.fixture
    def enclosure(self):
        return Enclosure("bird_house", 30, "aviary")

    def test_feed(self, zookeeper, bird, vet, enclosure, capsys):
        enclosure.add_animal(bird)
        zookeeper.add_enclosure(enclosure)
        zookeeper.add_animal(bird)
        vet.add_enclosure(enclosure)
        vet.add_animal(bird)

        zookeeper.perform_duties()
        test = capsys.readouterr()
        duties = test.out

        assert f"{bird.name} has been fed meat." in duties

        bird.is_sick = True
        zookeeper.perform_duties()
        test = capsys.readouterr()
        duties = test.out
        assert f"Unable to feed because {bird.name} is sick." in duties

        vet.perform_duties()
        test = capsys.readouterr()
        duties = test.out
        assert f"{bird.name} has been taken in for treatment." in duties







