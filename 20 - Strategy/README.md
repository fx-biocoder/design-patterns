# Strategy design pattern

## Description

The Strategy is a behavioral design pattern that defines a family of algorithms, encapsulates each one of them, and makes them interchangeable. It lets you select an algorithm's behavior at runtime. The pattern defines a common interface for different algorithms, allowing them to be used interchangeably without the client needing to know which specific algorithm is being executed.

## What specific problems do I solve using this pattern?

The Strategy pattern solves several important problems:

- It eliminates large conditional statements that select different algorithms based on runtime conditions, replacing them with polymorphic strategy classes.

- It makes it easy to add new algorithms or modify existing ones without changing the client code that uses them, adhering to the Open/Closed Principle.

- It allows algorithms to be selected at runtime, enabling dynamic behavior switching based on application requirements or user input.

- It makes code more maintainable and testable by isolating algorithm implementations in separate strategy classes, each with a single responsibility.

## Can I combine this design pattern with others? Which ones?

The Strategy pattern can be combined with several other design patterns:

- Factory Method: Factories can be used to create appropriate strategy instances based on context or user input.

- Decorator: Strategies can be decorated to add additional behavior like caching, logging, or validation.

- Template Method: Strategies can implement a template method to define a skeleton of the algorithm.

- Composite: Composite objects can use different strategies for aggregating results from their children.

## Contents of this section

The implementation in `main.py` demonstrates the Strategy pattern through a calculator application with the following components:

`Strategy`: Abstract interface defining the execute method that all concrete strategies must implement.

`ConcreteStrategyAdd`: Concrete strategy that implements addition operation between two numbers.

`ConcreteStrategySubtract`: Concrete strategy that implements subtraction operation between two numbers.

`ConcreteStrategyMultiply`: Concrete strategy that implements multiplication operation between two numbers.

`Context`: Class that maintains a reference to a strategy object and delegates the execution to it.

`Application`: Client application that allows users to select different strategies and execute operations interchangeably.

## License

This work is licensed under CC BY-NC-SA 4.0. See the LICENSE.md file for details.
