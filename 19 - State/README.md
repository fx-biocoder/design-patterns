# State design pattern

## Description

The State is a behavioral design pattern that allows an object to alter its behavior when its internal state changes. The pattern appears as if the object changed its class. It encapsulates different behaviors for different states and lets the object appear to change its type when the state changes. This is achieved by delegating state-specific behavior to state objects rather than using conditional statements.

## What specific problems do I solve using this pattern?

The State pattern solves several important problems:

- It eliminates complex conditional statements that would branch based on an object's current state, replacing them with polymorphic state classes.

- It allows you to add new states without modifying existing state classes, following the Open/Closed Principle and making the code more maintainable.

- It makes the code easier to understand by clearly separating the behavior of each state into distinct state classes rather than mixing them in the context class.

- It allows an object to change its behavior at runtime based on its current state, enabling dynamic behavior switching without changing the object's interface.

## Can I combine this design pattern with others? Which ones?

The State pattern can be combined with several other design patterns:

- Strategy: States are similar to strategies, but states can change automatically while strategies are typically selected by client code.

- Template Method: State implementations can use the Template Method pattern to define a skeleton of state behavior.

- Singleton: State objects can be implemented as singletons to ensure only one instance of each state exists.

- Factory Method: A factory can be used to create appropriate state objects based on context conditions.

- Observer: State changes can trigger notifications to observers about the new state.

## Contents of this section

The implementation in `main.py` demonstrates the State pattern through an audio player interface with the following components:

`State`: Abstract base class defining the interface for different states that an audio player can be in.

`ReadyState`: Concrete state representing a player that is ready to play or perform navigation operations.

`LockedState`: Concrete state representing a locked player that cannot play, skip, or navigate through songs.

`PlayingState`: Concrete state representing a player that is currently playing audio content.

`UserInterface`: Provides UI controls that delegate user actions to the current state of the audio player.

`AudioPlayer`: Context class that maintains the current state and delegates behavior based on that state.

## License

This work is licensed under CC BY-NC-SA 4.0. See the LICENSE.md file for details.
