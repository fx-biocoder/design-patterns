# Builder design pattern

## Description

The Builder pattern is a creational design pattern that lets you construct complex objects step by step. It allows you to produce different types and representations of an object using the same construction code. The pattern is particularly useful when you need to create an object with numerous possible configurations.

## What specific problems do I solve using this pattern?

The Builder pattern addresses several key problems in object creation:

- It provides a solution for handling complex object construction with many optional parameters and configurations. Instead of having multiple constructors or a single constructor with many parameters, the Builder pattern lets you construct objects step by step.

- It allows you to create different representations of objects using the same construction process. This is particularly useful when objects need to be constructed in different ways but follow similar steps.

- It isolates complex construction code from the object's business logic. The pattern encapsulates the way a complex object is constructed, allowing you to vary an object's internal representation.

## Can I combine this design pattern with others? Which ones?

The Builder pattern can be combined with several other design patterns:

- Abstract Factory: Builder can be used to create complex products within an Abstract Factory
- Composite: Builders are often used to build Composite trees or other complex objects
- Factory Method: Builder can be used as an alternative to Factory Method when you need more flexibility in object creation
- Singleton: The Director class in Builder pattern can be implemented as a Singleton
- Prototype: Builder can work with Prototype to copy complex objects instead of building them from scratch

## Contents of this section

The implementation in `main.py` demonstrates the Builder pattern through a flexible object construction system with the following components:

### Products:
- `Product1`: A complex object that can be constructed in various ways
- `Product2`: Another complex object with different configurations

### Abstract Builder:
- `Builder`: Abstract interface defining common construction steps:
  - `reset()`: Prepares the builder for a new construction
  - `build_step_a()`, `build_step_b()`, `build_step_z()`: Various construction steps

### Concrete Builders:
- `ConcreteBuilder1`: Implements the building steps for Product1
- `ConcreteBuilder2`: Implements the building steps for Product2
Each builder maintains a reference to the product being constructed and provides a method to retrieve the final result

### Director:
- Orchestrates the building process using a specific builder
- Defines different construction sequences ("simple" and "other")
- Can switch between different builders at runtime

### Helper Functions:
- `print_object()`: Utility function to display object properties
- `client()`: Demonstrates how to use the Builder pattern with different products

## License

This work is licensed under CC BY-NC-SA 4.0. See the LICENSE.md file for details.