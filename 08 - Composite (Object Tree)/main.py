"""
Composite Pattern - Design Patterns (GoF)

Author: Facundo Martínez (fx-biocoder)
Repository: https://github.com/fx-biocoder/design-patterns

Description:
This file contains an implementation for the Composite design pattern, one of the 23 design patterns described
by the Gang of Four (GoF). This pattern allows for implementing a tree-like structure of simple and/or complex objects
that share a common interface.
This code is based on the concepts and examples presented in the book "Dive Into Design Patterns" by Alexey Naumov.

Components:
- Graphic: Common interface for sub-elements.
- Dot: A sub-element that implements the Graphic interface.
- CompoundGraphic: The compound (a.k.a. container) that holds sub-elements while implementing the Graphic interface.
- Circle: A sub-element that extends the Dot sub-element.


License:
CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/deed.en)
"""
from abc import ABC, abstractmethod
from typing import List


class Graphic(ABC):
    @abstractmethod
    def move(self, x, y):
        raise NotImplementedError()

    @abstractmethod
    def draw(self):
        raise NotImplementedError()


class Dot(Graphic):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, x, y) -> None:
        self.x += x
        self.y += y

    def draw(self) -> None:
        print(f"Drawing a point at ({self.x}, {self.y})")


class CompoundGraphic(Graphic):
    def __init__(self):
        self.__children: List[Graphic] = []

    def add(self, child: Graphic) -> None:
        self.__children.append(child)

    def remove(self, child: Graphic) -> None:
        self.__children.remove(child)

    def move(self, x, y) -> None:
        for child in self.__children:
            child.move(x, y)

    def draw(self) -> None:
        for child in self.__children:
            child.draw()


class Circle(Dot):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def draw(self) -> None:
        print(f"Drawing a circle at ({self.x}, {self.y}, with radius {self.radius})")


def client() -> None:
    # Create individual figures
    dot = Dot(1, 2)
    circle = Circle(3, 4, 5)

    # Create a compound figure
    compound_graphic = CompoundGraphic()
    compound_graphic.add(dot)
    compound_graphic.add(circle)

    # Test the compound figure
    compound_graphic.draw()
    compound_graphic.move(1, 1)
    compound_graphic.draw()


if __name__ == "__main__":
    client()
