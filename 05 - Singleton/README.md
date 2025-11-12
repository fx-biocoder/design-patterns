# Singleton design pattern

## Description

The Singleton pattern is a creational design pattern that ensures a class has only one instance and provides a global point of access to that instance. It involves a class that manages its own instance and prevents any other class from creating new instances. The pattern is particularly useful when exactly one object is needed to coordinate actions across a system.

## What specific problems do I solve using this pattern?

The Singleton pattern addresses several key problems in software design:

- It ensures that a class has just one instance. This is crucial when exactly one object is needed to coordinate actions across the system, such as a database connection pool, file system, thread pool, or configuration manager.

- It provides a global access point to that instance. This allows the instance to be accessed from anywhere in the program while maintaining controlled access to the shared resource.

- It protects the instance from being overwritten by other code. The pattern implements controlled access to the sole instance, preventing other parts of the program from accidentally overwriting the global instance.

## Can I combine this design pattern with others? Which ones?

The Singleton pattern can be combined with several other design patterns:

- Abstract Factory: Singletons can be used to implement Abstract Factories
- Builder: The Director class in Builder pattern is often implemented as a Singleton
- Facade: The Facade class can be implemented as a Singleton since usually only one facade is needed
- Prototype: Prototype Registry is often implemented as a Singleton
State: State objects are often implemented as Singletons

## Contents of this section

The implementation in `main.py` demonstrates the Singleton pattern through a thread-safe metaclass implementation with the following components:

### Singleton Metaclass:
- `SingletonMeta`: A metaclass that implements the singleton behavior
  - Uses a dictionary to store instances of different classes
  - Implements thread-safe instance creation using a lock
  - Overrides the `__call__` method to control instance creation

### Example Classes:
- `MyClass`: A class using the SingletonMeta metaclass
  - Automatically gets singleton behavior from its metaclass
  - Any attempt to create new instances returns the same instance

- `OtherClass`: Another class using the SingletonMeta metaclass
  - Demonstrates that different classes can use the same singleton metaclass
  - Each class gets its own unique singleton instance

### Main Function:
- Demonstrates the usage of singleton classes
- Shows that multiple instantiation attempts return the same instance

## License

This work is licensed under CC BY-NC-SA 4.0. See the LICENSE.md file for details.