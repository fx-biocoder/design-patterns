"""
Builder Pattern - Design Patterns (GoF)

Author: Facundo Martínez (fx-biocoder)
Repository: https://github.com/fx-biocoder/design-patterns

Description:
This file contains an implementation for the Builder design pattern, one of the 23 design patterns described
by the Gang of Four (GoF). This pattern allows for constructing complex objects with multiple properties.
This code is based on the concepts and examples presented in the book "Dive Into Design Patterns" by Alexey Naumov.

Components:
- Product1 and Product2: Representing products with an arbitrary and potentially large number of properties. Their
  construction is delegated to specialized builder objects.
- Builder: Abstract interface that defines the steps that each builder has to execute.
- ConcreteBuilder1 and ConcreteBuilder2: Specific implementations of the Builder interface, which build instances of
  Product1 and Product2 respectively.
- Director: Object that orchestrates object building using a specific builder, defining different configurations
  according to the requested type. It is not strictly necessary to have one, but it is helpful for hiding details from
  the client code.


License:
CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/deed.en)
"""
from abc import ABC, abstractmethod


class Product1:
    """Product with an arbitrary, large number of properties"""
    pass


class Product2:
    """Product with an arbitrary, large number of properties"""
    pass


class Builder(ABC):
    """Common interface for concrete builders, with an arbitrary number of build steps.

    Note: It is important that this interface defines COMMON STEPS for all products.
    """
    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def build_step_a(self):
        pass

    @abstractmethod
    def build_step_b(self):
        pass

    @abstractmethod
    def build_step_z(self):
        pass


class ConcreteBuilder1(Builder):
    """Concrete builder for Product 1"""
    __result: Product1

    def reset(self) -> None:
        self.__result = Product1()

    def build_step_a(self) -> None:
        self.__result.property_a = "Value for Step A, Concrete Builder 1"

    def build_step_b(self) -> None:
        self.__result.property_b = "Value for Step B, Concrete Builder 1"

    def build_step_z(self) -> None:
        self.__result.property_z = "Value for Step Z, Concrete Builder 1"

    def get_result(self) -> Product1:
        return self.__result


class ConcreteBuilder2(Builder):
    """Concrete builder for Product 2"""
    __result: Product2

    def reset(self) -> None:
        self.__result = Product2()

    def build_step_a(self) -> None:
        self.__result.property_a = "Value for Step A, Concrete Builder 2"

    def build_step_b(self) -> None:
        self.__result.property_b = "Value for Step B, Concrete Builder 2"

    def build_step_z(self) -> None:
        self.__result.property_z = "Value for Step Z, Concrete Builder 2"

    def get_result(self) -> Product2:
        return self.__result


class Director:
    __builder: Builder

    def __init__(self, builder: Builder):
        self.__builder = builder

    def change_builder(self, builder: Builder) -> None:
        self.__builder = builder

    def make(self, obj_type: str) -> None:
        self.__builder.reset()

        if obj_type == "simple":
            self.__builder.build_step_a()
        else:
            self.__builder.build_step_b()
            self.__builder.build_step_z()


def print_object(obj) -> None:
    """Helper function for printing instance attributes"""
    print(vars(obj))


def client() -> None:
    # Testing first concrete builder
    builder = ConcreteBuilder1()
    director = Director(builder)
    director.make("simple")

    product_a: Product1 = builder.get_result()
    print_object(product_a)

    # Changing to second concrete builder
    builder_b = ConcreteBuilder2()
    director.change_builder(builder_b)
    director.make("other")

    product_b: Product2 = builder_b.get_result()
    print_object(product_b)


if __name__ == "__main__":
    client()
