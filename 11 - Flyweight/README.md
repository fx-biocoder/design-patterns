# Flyweight design pattern

## Description

The Flyweight pattern is a structural design pattern that minimizes memory usage by sharing as much data as possible with similar objects. It separates intrinsic state (shared) from extrinsic state (context-specific) and stores the shared state in flyweight objects that multiple concrete objects reference.

## What specific problems do I solve using this pattern?

The Flyweight pattern addresses situations where a large number of objects must be created and these objects contain duplicated data. By extracting and sharing the common parts of the state, it reduces memory usage and improves performance in memory-constrained environments.

## Can I combine this design pattern with others? Which ones?

The Flyweight pattern can be combined with several other patterns:

- Factory Method or Abstract Factory: Factories can be used to manage or create flyweight objects
- Prototype: Flyweights can be cloned from prototype instances when necessary
- Composite: Flyweights can be used to represent leaf objects within a Composite tree
- Singleton: The Flyweight factory is often implemented as a Singleton to provide a global point of access

## Contents of this section

The implementation in `main.py` demonstrates the Flyweight pattern through a tree/forest example with the following components:

`TreeType`: Represents the flyweight that stores intrinsic state for trees, such as name, color, and texture. It provides a `draw()` method that receives extrinsic context like coordinates and canvas.

`Tree`: Represents concrete tree objects that hold extrinsic state (x and y coordinates) and a reference to a shared `TreeType`. It inherits from `TreeType` for convenience and provides a static `draw()` helper.

`TreeFactory`: Manages creation and reuse of `TreeType` instances. It returns an existing `TreeType` for a given key of (name, color, texture) or creates a new one when needed, logging creation or reuse.

`Forest`: Manages a collection of `Tree` instances and uses a `TreeFactory` to obtain shared `TreeType` instances when planting trees. It provides a `draw()` method to render all trees onto a canvas.

## License

This work is licensed under CC BY-NC-SA 4.0. See the LICENSE.md file for details.