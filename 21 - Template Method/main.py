"""
Template Method Pattern - Design Patterns (GoF)

Author: Facundo Martínez (fx-biocoder)
Repository: https://github.com/fx-biocoder/design-patterns

Description:
This file contains an implementation for the Observer design pattern, one of the 23 design patterns described by the
Gang of Four (GoF). This pattern allows for defining the scaffold of an algorithm in the superclass but allows for
the subclasses to overwrite algorithm steps without changing its structure.
This code is based on the concepts and examples presented in the book "Dive Into Design Patterns" by Alexey Naumov.

Components:
- GameAI: Abstract template class that defines the skeleton of the AI turn algorithm.
- OrcsAI: Concrete implementation of GameAI.
- MonstersAI: Another concrete implementation of GameAI.

License:
CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/deed.en)
"""
from abc import ABC, abstractmethod


class GameAI(ABC):
    def __init__(self):
        self.built_structures = []

    @abstractmethod
    def build_structures(self):
        raise NotImplementedError

    @abstractmethod
    def build_units(self):
        raise NotImplementedError

    @abstractmethod
    def send_scouts(self, position):
        raise NotImplementedError

    @abstractmethod
    def send_warriors(self, position):
        raise NotImplementedError

    @staticmethod
    def closest_enemy():
        # Logic goes here
        return "Enemy found"

    @staticmethod
    def map_center() -> tuple[int, int]:
        # Depends on game implementation
        return 0, 0

    def collect_resources(self) -> None:
        for structure in self.built_structures:
            structure.collect()

    def attack(self) -> None:
        enemy = self.closest_enemy()
        if not enemy:
            self.send_scouts(self.map_center())
        else:
            self.send_warriors(enemy)

    def turn(self) -> None:
        self.collect_resources()
        self.build_structures()
        self.build_units()
        self.attack()


class OrcsAI(GameAI):
    def __init__(self):
        super().__init__()
        self.scouts = []
        self.warriors = []
        self.resources = {
            "food": 100,
            "ore": 100,
            "gold": 100,
            "wood": 100
        }

    @staticmethod
    def resources_available() -> bool:
        # Logic goes here
        return True

    def have_scouts(self) -> bool:
        return len(self.scouts) > 0

    def have_warriors(self) -> bool:
        return len(self.warriors) > 0

    def create_peasant_and_add_to_scouts(self) -> None:
        self.scouts.append("Peasant")
        print("Adding peasant to scouts...")

    def create_soldier_and_add_to_warriors(self) -> None:
        self.warriors.append("Soldier")
        print("Adding soldier to warriors...")

    def build_units(self) -> None:
        if self.resources_available():
            if not self.have_scouts():
                self.create_peasant_and_add_to_scouts()
            else:
                self.create_soldier_and_add_to_warriors()

    def send_scouts(self, position) -> None:
        if len(self.scouts) > 0:
            # Logic goes here
            print(f"Sending scouts to {position}")

    def send_warriors(self, position) -> None:
        if len(self.warriors) > 0:
            # Logic goes here
            print(f"Sending warriors to {position}")

    def build_farm(self) -> None:
        if self.resources_available():
            print("Building farm")
        else:
            print("Not enough resources!")

    def build_barracks(self) -> None:
        if self.resources_available():
            print("Building barracks")

    def build_fortress(self) -> None:
        if self.resources_available():
            print("Building fortress")

    def build_structures(self) -> None:
        self.build_farm()
        self.build_barracks()
        self.build_fortress()


class MonstersAI(GameAI):
    def collect_resources(self) -> None:
        print("Monsters do not collect resources")

    def build_structures(self) -> None:
        print("Monsters do not build structures")

    def build_units(self) -> None:
        print("Monsters do not build units")

    def send_scouts(self, position) -> None:
        print("Monsters do not send scouts")

    def send_warriors(self, position) -> None:
        print("Monsters do not send warriors")


if __name__ == "__main__":
    orcs = OrcsAI()
    orcs.turn()

    monsters = MonstersAI()
    monsters.turn()