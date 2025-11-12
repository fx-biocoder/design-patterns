# Memento design pattern

## Description

The Memento is a behavioral design pattern that allows you to save and restore the previous states of an object without violating the principle of encapsulation. The pattern provides a way to capture an object's internal state and externalize it so that the object can be restored to this state later. It accomplishes this without exposing the details of the object's implementation.

## What specific problems do I solve using this pattern?

The Memento pattern solves several important problems:

- It allows you to implement undo and redo functionality by capturing and restoring the internal state of objects at different points in time.

- It provides a way to save object state without violating encapsulation, by allowing an object to create snapshots of its internal state that other objects cannot directly access or modify.

- It enables you to implement checkpoint systems where the state of a system can be saved and restored, which is useful for applications like text editors, game engines, and transaction systems.

- It allows you to rollback changes made to an object by restoring it to a previously saved state, providing a clean and organized way to handle state reversions.

## Can I combine this design pattern with others? Which ones?

The Memento pattern can be combined with several other design patterns:

- Command: Commands can create and store mementos to implement undo and redo operations.

- Iterator: Iterators can traverse through a series of memento objects to replay state changes.

- Prototype: Mementos can be used to clone the state of complex objects.

- Observer: The Observer pattern can be used to notify listeners when state snapshots are created or restored.

- Singleton: A caretaker can be implemented as a singleton to manage all mementos in the application.

## Contents of this section

The implementation in `main.py` demonstrates the Memento pattern through a text editor example with the following components:

`Snapshot`: Encapsulates the state of an Editor at a particular moment, storing text, cursor position, and selection width immutably.

`Editor`: Originator class that maintains its internal state including text, cursor position, and selection width, and creates snapshots of this state.

`Command`: Caretaker class that manages memento backups, allowing undo operations by restoring saved states.

## License

This work is licensed under CC BY-NC-SA 4.0. See the LICENSE.md file for details.
