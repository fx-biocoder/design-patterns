# Abstract Factory design pattern

## Description

The Abstract Factory is a creational design pattern that provides an interface for creating families of related or dependent objects without specifying their concrete classes. It allows a system to be independent of how its products are created, composed, and represented, while ensuring that the created products are compatible with each other.

## What specific problems do I solve using this pattern?

The Abstract Factory pattern solves several important problems in software design:

- It provides a way to create families of related objects without specifying their concrete classes. This is particularly useful when your system needs to be independent of how its products are created and composed.

- It ensures compatibility between products of the same family. When your application needs to use products that belong to a coherent family or theme (like UI elements matching a specific style), this pattern guarantees that the products will always be compatible.

- It helps in managing product variations. When you have multiple families of products and need to ensure that the products used together are from the same family, this pattern makes it easier to switch between different product families.

## Can I combine this design pattern with others? Which ones?

- The Abstract Factory pattern can be effectively combined with several other design patterns:

- Factory Method: Abstract Factory classes are often implemented using Factory Methods
- Singleton: An Abstract Factory can be implemented as a Singleton when exactly one instance is needed
- Builder: Abstract Factory can be used with Builder when the products need complex construction steps
- Prototype: Abstract Factory can use Prototype to create objects by cloning a prototype
- Bridge: Abstract Factory can be used together with Bridge when you need to create platform-independent class hierarchies

## Contents of this section

The implementation in `main.py` demonstrates the Abstract Factory pattern through a furniture manufacturing example with the following components:

### Abstract Products:
- `Chair`: Interface defining common chair operations (`has_legs()`, `sit_on()`)
- `Sofa`: Interface defining common sofa operations (`has_legs()`, `sit_on()`)
- `Table`: Interface defining common table operations (`has_legs()`, `get_style()`)

### Concrete Products:
- Victorian style products:
  - `VictorianChair`
  - `VictorianSofa`
  - `VictorianTable`
- Modern style products:
  - `ModernChair`
  - `ModernSofa`
  - `ModernTable`

### Abstract Factory:
- `FurnitureFactory`: Abstract interface for creating furniture with methods:
  - `create_chair()`
  - `create_sofa()`
  - `create_table()`

### Concrete Factories:
- `VictorianFurnitureFactory`: Creates Victorian-style furniture
- `ModernFurnitureFactory`: Creates Modern-style furniture

### Helper function:
- `call_factories()`: Demonstrates how client code works with factories and their products

## License

This work is licensed under CC BY-NC-SA 4.0. See the LICENSE.md file for details.