# Adapter design pattern

## Description

The Adapter pattern is a structural design pattern that allows objects with incompatible interfaces to collaborate. It acts as a wrapper between two objects, catching calls for one object and transforming them to format and interface recognizable by the second object. This pattern is particularly useful when you want to use an existing class, but its interface isn't compatible with the rest of your code.

## What specific problems do I solve using this pattern?

The Adapter pattern addresses several important problems in software design:

- It enables the integration of incompatible interfaces. When you need to use a class that doesn't match the interface your code expects, an adapter can bridge this gap by wrapping the incompatible class in a way that makes it compatible.

- It helps in reusing existing code with incompatible interfaces. Instead of rewriting existing code to match a new interface, you can create an adapter that makes the existing code work with the new interface.

- It facilitates system integration when working with legacy code or third-party libraries. When integrating different systems or libraries with different interfaces, adapters can make them work together without modifying their source code.

## Can I combine this design pattern with others? Which ones?

The Adapter pattern can be effectively combined with several other design patterns:

- Bridge: Adapter is often used in systems where Bridge pattern is already present
- Decorator: Adapter changes the interface of an object, while Decorator enhances it without changing the interface
- Composite: Adapter can make incompatible objects work with a Composite structure
- Facade: Adapter adapts an existing interface while Facade defines a new one
- Proxy: Adapter provides a different interface to an object while Proxy provides the same interface

## Contents of this section

The implementation in `main.py` demonstrates the Adapter pattern through a geometric shapes example with the following components:

### Target Interface:
- `RoundPeg`: Defines the interface that clients work with
  - `get_radius()`: Returns the radius of the peg

### Client:
- `RoundHole`: Works with round pegs through the target interface
  - `fits(peg)`: Checks if a round peg fits in the hole

### Adaptee:
- `SquarePeg`: Incompatible class with a different interface
  - `get_width()`: Returns the width of the square peg
  - Not directly compatible with RoundHole

### Adapter:
- `SquarePegAdapter`: Makes SquarePeg compatible with RoundHole
  - Extends RoundPeg to maintain interface compatibility
  - Contains reference to the adapted SquarePeg
  - Converts square peg measurements to round peg radius
  - Uses mathematical formula to calculate equivalent radius

### Client Code:
- Demonstrates usage of both regular round pegs and adapted square pegs
- Shows how adapter makes incompatible objects work together
- Illustrates size compatibility checks with different peg sizes

## License

This work is licensed under CC BY-NC-SA 4.0. See the LICENSE.md file for details.