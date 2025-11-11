# Factory Method design pattern

## Description

The Factory Method is a creational design pattern that provides an interface for creating objects in a superclass while allowing subclasses to alter the type of objects that will be created. It encapsulates object creation logic in a separate method, which subclasses can override to change the type of objects being created.

## What specific problems do I solve using this pattern?

The Factory Method pattern solves several key problems in software design:

- The pattern eliminates tight coupling between the creator and concrete product classes. Code that needs to create objects can work with any concrete product through the common product interface, without being tied to specific classes.

- It centralizes product creation code in one place, making the code easier to support and maintain. When you need to add new product types, you only need to create a new factory subclass.

- It implements the Open/Closed Principle by allowing you to introduce new types of products into the program without breaking existing client code.

## Can I combine this design pattern with others? Which ones?

The Factory Method pattern can be effectively combined with several other design patterns:

- Abstract Factory: Factory Methods are often used within Abstract Factories to create their products.
- Template Method: Factory Method is a specialization of Template Method.
- Prototype: Factory Method can use Prototype to create objects by cloning a pre-built prototype.
- Builder: Factory Method can be used to create complex objects step by step using the Builder pattern.
- Singleton: The Factory Method can return a Singleton instance instead of creating new objects.

## Contents of this section

The implementation in `main.py` demonstrates the Factory Method pattern through a GUI dialog example with the following components:

### Button (Abstract Class):
- Defines the interface for buttons with abstract methods `on_click()` and `render()`
- Serves as the base product class

### WindowsButton and HTMLButton (Concrete Classes):
- Concrete implementations of the Button interface for different platforms
- Implement specific rendering and click behavior

### Dialog (Abstract Class):
- The abstract creator class containing the factory method
- Defines the abstract `create_button()` method
- Implements a template method `render()` that uses the factory method

### WindowsDialog and WebDialog (Concrete Classes):
- Concrete creator classes that override the factory method
- Each returns its corresponding button type (WindowsButton or HTMLButton)

Helper function `render_dialog()`:
- Demonstrates how client code works with factories and products

## License

This work is licensed under CC BY-NC-SA 4.0. See the LICENSE.md file for details.