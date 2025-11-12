"""
Strategy Pattern - Design Patterns (GoF)

Author: Facundo Martínez (fx-biocoder)
Repository: https://github.com/fx-biocoder/design-patterns

Description:
This file contains an implementation for the Strategy design pattern, one of the 23 design patterns described by the
Gang of Four (GoF). This pattern allows for defining a family of algorithms, placing each of them in separate classes,
and use their objects interchangeably.
This code is based on the concepts and examples presented in the book "Dive Into Design Patterns" by Alexey Naumov.

Components:
- Strategy: Abstract interface defining the execute method that all concrete strategies must implement.
- ConcreteStrategyAdd: Concrete strategy that implements addition operation between two numbers.
- ConcreteStrategySubtract: Concrete strategy that implements subtraction operation between two numbers.
- ConcreteStrategyMultiply: Concrete strategy that implements multiplication operation between two numbers.
- Context: Class that maintains a reference to a strategy object and delegates the execution to it.
- Application: Client application that allows users to select different strategies.

License:
CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/deed.en)
"""
from abc import ABC, abstractmethod


class Strategy(ABC):
    @abstractmethod
    def execute(self, a, b):
        raise NotImplementedError


class ConcreteStrategyAdd(Strategy):
    def execute(self, a, b):
        return a + b


class ConcreteStrategySubtract(Strategy):
    def execute(self, a: float, b: float):
        return a - b


class ConcreteStrategyMultiply(Strategy):
    def execute(self, a: float, b: float):
        return a * b


class Context:
    def __init__(self, strategy: Strategy | None = None):
        self.strategy = strategy

    def set_strategy(self, strategy: Strategy):
        self.strategy = strategy

    def execute_strategy(self, a: float, b: float):
        return self.strategy.execute(a, b)


class Application:
    def __init__(self):
        self.context = Context()

    def main(self):
        a: int = int(input("Enter the first number: "))
        b: int = int(input("Enter the second number: "))
        action: str = input("Enter the action (add, subtract, multiply): ").lower()

        match action:
            case "add":
                self.context.set_strategy(ConcreteStrategyAdd())
            case "subtract":
                self.context.set_strategy(ConcreteStrategySubtract())
            case "multiply":
                self.context.set_strategy(ConcreteStrategyMultiply())

        result = self.context.execute_strategy(a, b)
        print(f"Result: {str(result)}")


if __name__ == "__main__":
    application = Application()
    application.main()
