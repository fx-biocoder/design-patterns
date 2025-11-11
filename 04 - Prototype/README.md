# Prototype design pattern

## Description

The Prototype pattern is a creational design pattern that lets you copy existing objects without making your code dependent on their classes. It delegates the cloning process to the actual objects that are being cloned instead of creating objects from scratch. The pattern provides a mechanism to copy an original object and creates a clone that is a exact copy of the original object.

## What specific problems do I solve using this pattern?

The Prototype pattern addresses several important problems in object creation:

- It helps when you need to create objects based on existing objects while keeping the creation process independent of the concrete classes. This is particularly useful when the creation of a new object is more efficient through copying than through creation from scratch.

- It reduces the complexity of creating objects that require complex initialization or configuration. Instead of recreating an object with the same configuration multiple times, you can clone an already configured object.

- It provides a way to create copies of objects whose exact type might not be known at compile time. The pattern allows a system to create new objects by cloning a prototypical instance, regardless of the concrete class of the prototype.

## Can I combine this design pattern with others? Which ones?

The Prototype pattern can be effectively combined with several other design patterns:

- Abstract Factory: Prototype can be used to implement Abstract Factories by storing a set of prototypical objects
- Command: Prototype can be used to store command history by making deep copies of commands
- Composite: Prototype can be used to clone complex composite structures efficiently
- Factory Method: Prototype can serve as an alternative to Factory Method when dealing with many possible classes
Singleton: A prototype registry is often implemented as a Singleton

## Contents of this section

The implementation in `main.py` demonstrates the Prototype pattern through a flexible object cloning system with the following components:

### Prototype Interface:
- `Prototype`: Abstract base class defining the cloning interface
  - `clone()`: Abstract method that concrete prototypes must implement

### Prototype Registry:
- `PrototypeRegistry`: Manages a collection of prototype objects
  - `add_item()`: Registers new prototypes
  - `get_by_field1()`: Retrieves clones based on field1 value
  - `get_by_field2()`: Retrieves clones based on field2 value

### Concrete Prototypes:
- `ConcretePrototype`: Basic implementation of the Prototype interface
  - Implements deep copying through `clone()`
  - Manages a field1 property
  - Includes copy constructor for prototype-based initialization

- `SubclassPrototype`: Extended implementation inheriting from ConcretePrototype
  - Adds field2 property
  - Implements its own cloning mechanism

### Helper Functions:
- `client()`: Demonstrates the usage of prototypes and the registry:
  - Creating and cloning objects
  - Using the prototype registry
  - Retrieving clones based on field values

## License

This work is licensed under CC BY-NC-SA 4.0. See the LICENSE.md file for details.