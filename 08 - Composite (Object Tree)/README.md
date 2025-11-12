# Composite (Object Tree) design pattern

## Description

The Composite pattern is a structural design pattern that lets you compose objects into tree structures and then work with these structures as if they were individual objects. It allows you to treat both individual objects and compositions of objects uniformly. The pattern creates a class hierarchy of simple and composite objects, making it easier to build complex tree structures with varying levels of nesting.

## What specific problems do I solve using this pattern?

The Composite pattern solves several important problems in software design:

- It provides a unified way to treat both simple and complex elements in a tree structure. Clients can treat individual objects and compositions of objects uniformly, simplifying client code.

- It makes it easy to add new kinds of components to the system without breaking existing code. New types of leaves or composites can be added by implementing the common interface.

- It helps in building complex tree-like structures of objects where parts of the structure can be treated the same as the whole. This is particularly useful in scenarios like graphical user interfaces, file systems, or organizational structures.

## Can I combine this design pattern with others? Which ones?

The Composite pattern can be combined with several other design patterns:

- Builder: Can be used to construct complex Composite trees step by step
- Iterator: Can be used to traverse Composite trees
- Visitor: Can be used to execute operations over a Composite tree
Chain of Responsibility: Component parents can act as links in the chain
- Decorator: Both patterns have similar structure diagrams and can be used together to enhance components
- Flyweight: Can be used to share leaf components in a Composite tree

## Contents of this section

The implementation in `main.py` demonstrates the Composite pattern through a graphical shapes system with the following components:

### Component Interface:
- `Graphic`: Abstract base class defining operations for all elements
  - `move(x, y)`: Moves the graphic element
  - `draw()`: Renders the graphic element

### Leaf Elements:
- `Dot`: Basic graphical element
  - Represents a point in 2D space
  - Implements basic move and draw operations

- `Circle`: Extended leaf element
  - Inherits from Dot
  - Adds radius property
  - Overrides draw operation for circle-specific rendering

### Composite:
- `CompoundGraphic`: Container for multiple graphics
  - Maintains a collection of child components
  - Implements the same interface as leaf elements
  - Delegates operations to child components
  - Provides methods to manage children (add/remove)

### Client Code:
- Demonstrates creation of simple and compound graphics
- Shows uniform treatment of individual and composite objects
- Tests operations on both types of objects:
  - Drawing individual and compound elements
  - Moving elements in the hierarchy

## License

This work is licensed under CC BY-NC-SA 4.0. See the LICENSE.md file for details.