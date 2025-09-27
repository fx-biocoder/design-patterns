"""
Prototype Pattern - Design Patterns (GoF)

Author: Facundo Martínez (fx-biocoder)
Repository:

Description:
This file contains an implementation for the Prototype design pattern, one of the 23 design patterns described
by the Gang of Four (GoF). This pattern allows for delegating the cloning process to the objects that are being cloned
instead of manually creating exact copies.
This code is based on the concepts and examples presented in the book "Dive Into Design Patterns" by Alexey Naumov.

Components:
- Prototype: Common interface for prototypes
- PrototypeRegistry: This object registries the current prototypes
- ConcretePrototype: Implementation of the Prototype interface
- SubclassConcretePrototype: Class that inherits from ConcretePrototype


License:
CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/deed.en)
"""
import copy
from abc import ABC, abstractmethod
from typing import List, Union, Self


class Prototype(ABC):
    @abstractmethod
    def clone(self):
        pass


class PrototypeRegistry:
    def __init__(self):
        self.__items: List[Prototype] = []

    def add_item(self, prototype: Prototype):
        self.__items.append(prototype)

    def get_by_field1(self, value) -> Union[Prototype, None]:
        """Retrieves a clone of the prototype where field1=value

        NOTE: The pseudocode in Naumov's book returns a clone of the first matching prototype, but there could be
        several matches. In a scenario where several prototypes have the same value for field1, the filtering condition
        should inspect several fields. For simplicity, I will follow the example in the book.
        """
        for prototype in self.__items:
            # noinspection PyUnresolvedReferences
            if prototype.field1 == value:
                return prototype.clone()

        return None

    def get_by_field2(self, value) -> Union[Prototype, None]:
        """Retrieves a clone of the prototype where field2=value"""
        for prototype in self.__items:
            # noinspection PyUnresolvedReferences
            if prototype.field2 == value:
                return prototype.clone()

        return None


class ConcretePrototype(Prototype):
    """Concrete implementation of the Prototype interface"""
    def __init__(self, prototype=None):
        # A prototype class has to define a non-default constructor that takes a prototype
        # I don't like this direct reference, but for simplicity I leave it as is
        # Ideally the prototype should have a getter for retrieving field1
        if prototype:
            self.field1 = prototype.field1
        else:
            self.field1 = None

    def clone(self) -> Self:
        """Implementation of the clone method"""
        return copy.deepcopy(self)


class SubclassPrototype(ConcretePrototype):
    def __init__(self, prototype):
        super().__init__(prototype)
        self.field2 = prototype.field2

    def clone(self) -> Self:
        """The implementation should be very similar to that of ConcretePrototype.clone()
        Still, you can modify it according to your specific needs"""
        return copy.deepcopy(self)


def client():
    # Cloning a prototype
    obj = ConcretePrototype()
    new_copy = obj.clone()

    # Adding prototype to the registry
    registry = PrototypeRegistry()
    registry.add_item(obj)
    registry.add_item(new_copy)

    # Get prototypes from registry
    retrieve_prototype = registry.get_by_field1(value=None)
    print(retrieve_prototype)


if __name__ == "__main__":
    client()
