"""
Abstract Factory Pattern - Design Patterns (GoF)

Author: Facundo Martínez (fx-biocoder)
Repository: https://github.com/fx-biocoder/design-patterns

Description:
This file contains an implementation for the Abstract Factory design pattern, one of the 23 design patterns described
by the Gang of Four (GoF). This pattern provides an interface to create families of related or dependent products,
without specifying their concrete implementations. This pattern is useful for guaranteeing coherence between products
of the same family.
This code is based on the concepts and examples presented in the book "Dive Into Design Patterns" by Alexey Naumov.

Components:
- Abstract products: Chair, Sofa, Table
- Concrete products: Victorian (chair, sofa, table), Modern (chair, sofa, table)
- Abstract factory: FurnitureFactory
- Concrete factories: VictorianFurnitureFactory, ModernFurnitureFactory

License:
CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/deed.en)
"""
from abc import ABC, abstractmethod


class Chair(ABC):
    """Common interface for all Chairs"""
    @abstractmethod
    def has_legs(self):
        pass

    @abstractmethod
    def sit_on(self):
        pass


class VictorianChair(Chair):
    """Implementation of Victorian chairs"""
    def has_legs(self) -> bool:
        return True

    def sit_on(self) -> None:
        print("Sitting on Victorian chair")


class ModernChair(Chair):
    """Implementation of Modern chairs"""
    def has_legs(self) -> bool:
        return False

    def sit_on(self) -> None:
        print("Sitting on Modern chair")


class Sofa(ABC):
    """Common interface for all Sofa objects"""
    @abstractmethod
    def has_legs(self):
        pass

    @abstractmethod
    def sit_on(self):
        pass


class VictorianSofa(Sofa):
    """Implementation of Victorian sofa"""
    def has_legs(self) -> bool:
        return True

    def sit_on(self):
        print("Sitting on Victorian sofa")


class ModernSofa(Sofa):
    """Implementation of Modern sofa"""
    def has_legs(self) -> bool:
        return True

    def sit_on(self):
        print("Sitting on Modern sofa")


class Table(ABC):
    """Common interface for all Table objects"""
    @abstractmethod
    def has_legs(self):
        pass

    @abstractmethod
    def get_style(self):
        pass


class VictorianTable(Table):
    """Implementation of Victorian table"""
    def has_legs(self) -> bool:
        return True

    def get_style(self) -> None:
        print("Victorian Table")


class ModernTable(Table):
    """Implementation of Modern table"""
    def has_legs(self) -> bool:
        return False

    def get_style(self) -> None:
        print("Modern Table")


class FurnitureFactory(ABC):
    """Common interface for furniture factories"""
    @abstractmethod
    def create_chair(self) -> Chair:
        pass

    @abstractmethod
    def create_sofa(self) -> Sofa:
        pass

    @abstractmethod
    def create_table(self) -> Table:
        pass


class VictorianFurnitureFactory(FurnitureFactory):
    """Factory for Victorian furniture"""
    def create_chair(self) -> VictorianChair:
        return VictorianChair()

    def create_sofa(self) -> VictorianSofa:
        return VictorianSofa()

    def create_table(self) -> VictorianTable:
        return VictorianTable()


class ModernFurnitureFactory(FurnitureFactory):
    """Factory for Modern furniture"""
    def create_chair(self) -> ModernChair:
        return ModernChair()

    def create_sofa(self) -> ModernSofa:
        return ModernSofa()

    def create_table(self) -> ModernTable:
        return ModernTable()


def call_factories(factory: FurnitureFactory) -> None:
    """Helper function that simulates calls to the abstract furniture factory."""
    chair = factory.create_chair()
    sofa = factory.create_sofa()
    table = factory.create_table()

    chair.sit_on()
    sofa.sit_on()
    table.get_style()


if __name__ == "__main__":
    call_factories(VictorianFurnitureFactory())
    call_factories(ModernFurnitureFactory())
