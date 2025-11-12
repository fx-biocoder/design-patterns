# Iterator design pattern

## Description

The Iterator is a behavioral design pattern that lets you traverse elements of a collection without exposing its underlying representation. It provides a way to access the elements of an aggregate object sequentially without exposing its underlying representation. The pattern encapsulates the traversal logic and allows you to iterate through different collection types using a uniform interface.

## What specific problems do I solve using this pattern?

The Iterator pattern solves several important problems:

- It allows you to traverse elements of collections without knowing their internal structure, whether they are lists, trees, graphs, or any other data structure.

- It decouples the collection's interface from the traversal algorithms, allowing you to change or add new traversal strategies without modifying the collection classes.

- It enables you to have multiple simultaneous iterations over the same collection, with each iterator maintaining its own state independently.

- It provides a uniform way to access elements across different collection types, allowing client code to work with any iterable collection through a common interface.

## Can I combine this design pattern with others? Which ones?

The Iterator pattern can be combined with several other design patterns:

- Composite: Iterators can traverse complex tree structures created with the Composite pattern, providing uniform access to leaf and composite nodes.

- Factory Method: Factory methods can create appropriate iterator instances for different collection types.

- Strategy: Different iteration strategies can be encapsulated as separate iterator implementations.

- Memento: Iterator state can be captured and restored using the Memento pattern for resumable iterations.

## Contents of this section

The implementation in `main.py` demonstrates the Iterator pattern through social network examples with the following components:

`Profile`: Represents a user profile with identifier and email information that can be iterated over.

`ProfileIterator`: Abstract interface defining methods to iterate through profile collections.

`SocialNetwork`: Abstract interface for creating iterators specific to different relationship types.

`FacebookIterator`: Concrete iterator implementation that traverses Facebook profiles with lazy initialization.

`SocialSpammer`: Client class that uses iterators to send messages to profile collections without accessing them directly.

`Facebook`: Concrete social network that creates FacebookIterator instances for different relationship types.

`LinkedIn`: Another concrete social network implementation example for reference.

`Application`: Client application that demonstrates using different social networks and sending spam through iterators.

## License

This work is licensed under CC BY-NC-SA 4.0. See the LICENSE.md file for details.
