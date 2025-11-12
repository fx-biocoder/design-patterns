# Bridge design pattern

## Description

The Bridge pattern is a structural design pattern that lets you split a large class or a set of closely related classes into two separate hierarchies—abstraction and implementation—which can be developed independently of each other. The pattern involves creating a bridge interface that uses composition instead of inheritance to separate the abstraction from its implementation.

## What specific problems do I solve using this pattern?

The Bridge pattern solves several important problems in software design:

- It helps to avoid a permanent binding between an abstraction and its implementation. This is particularly useful when the implementation must be selected or switched at run-time.

- It prevents the explosion of classes that can occur when using inheritance to handle multiple orthogonal dimensions of variation. Instead of creating a new class for each combination of variations, you can combine them through composition.

- It improves extensibility by allowing you to extend the abstraction and implementation hierarchies independently. New implementations can be added without modifying the abstraction code, and new abstractions can be added without touching the implementation code.

## Can I combine this design pattern with others? Which ones?

The Bridge pattern can be combined with several other design patterns:

- Abstract Factory: Can be used to create and configure specific Bridge implementations
- Adapter: Bridge is designed up-front to let abstractions and implementations vary independently, while Adapter is commonly used with existing code
- State: Bridge can work with State to let implementation switching happen independently of the abstraction
- Strategy: Bridge has a similar structure to Strategy but serves a different purpose
- Observer: Bridge can be used with Observer to maintain independence between the abstraction and its implementation while still allowing them to communicate

## Contents of this section

The implementation in `main.py` demonstrates the Bridge pattern through a device remote control system with the following components:

### Implementation Interface:
- `Device`: Abstract base class defining device operations
  - Basic device controls (enable/disable)
  - Volume controls
  - Channel controls

### Concrete Implementations:
- `Televisor`: Concrete implementation for TV devices
- `Radio`: Concrete implementation for radio devices

### Abstraction:
- `RemoteControl`: Base abstraction class
  - Holds reference to device implementation
  - Provides high-level control operations
  - Delegates actual work to the device implementation

### Refined Abstraction:
- `AdvancedRemoteControl`: Extended remote control functionality
  - Adds additional features (mute)
  - Works with any device implementation

### Client Code:
- Shows how to use different combinations of devices and remotes
- Demonstrates the flexibility of switching implementations

## License

This work is licensed under CC BY-NC-SA 4.0. See the LICENSE.md file for details.