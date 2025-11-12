# Template Method design pattern

## Description

The Template Method is a behavioral design pattern that defines the skeleton of an algorithm in a base class but lets subclasses override specific steps of the algorithm without changing its structure. It uses inheritance to vary parts of the algorithm while keeping its overall structure unchanged. The pattern encourages code reuse and makes it easy to extend algorithms by creating subclasses that implement specific steps.

## What specific problems do I solve using this pattern?

The Template Method pattern solves several important problems:

- It eliminates duplication of common algorithm structure across multiple classes by centralizing it in a base template method.

- It allows subclasses to override only the specific steps of an algorithm that differ, while inheriting the common structure from the parent class.

- It defines the points of extension in an algorithm, making it clear where subclasses can customize behavior without allowing them to modify the overall algorithm structure.

- It enforces consistent algorithm structure across different implementations, ensuring that all subclasses follow the same sequence of steps.

## Can I combine this design pattern with others? Which ones?

The Template Method pattern can be combined with several other design patterns:

- Strategy: Template Method defines algorithms through inheritance while Strategy uses composition for algorithm variation.

- Factory Method: Template methods often use factory methods to create objects needed for algorithm steps.

- Decorator: Template methods can be used to implement decorated behavior chains.

- Command: Different commands can implement the steps of a template algorithm.

## Contents of this section

The implementation in `main.py` demonstrates the Template Method pattern through a game AI system with the following components:

`GameAI`: Abstract template class that defines the skeleton of the AI turn algorithm with abstract methods for subclasses to implement.

`OrcsAI`: Concrete implementation of GameAI that defines how Orcs build structures, units, and engage in combat within the template structure.

`MonstersAI`: Another concrete implementation of GameAI demonstrating how different AI types can override template steps to create completely different behaviors.

## License

This work is licensed under CC BY-NC-SA 4.0. See the LICENSE.md file for details.
