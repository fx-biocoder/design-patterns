# Decorator design pattern

## Description

The Decorator pattern is a structural design pattern that lets you dynamically add new behaviors to objects by placing these objects inside special wrapper objects that contain the behaviors. It provides a flexible alternative to subclassing for extending functionality, allowing you to add responsibilities to objects at runtime instead of statically through inheritance.

## What specific problems do I solve using this pattern?

The Decorator pattern solves several important problems in software design:

- It provides a flexible alternative to subclassing for extending functionality. Instead of creating multiple subclasses for every possible combination of features, you can create several decorator classes that can be combined in various ways.

- It allows responsibilities to be added to objects dynamically at runtime. You can add or remove responsibilities from an object without affecting other objects of the same class.

- It supports the Single Responsibility Principle by allowing functionality to be divided into classes. Instead of having a monolithic class with all possible variants of behavior, you can have several decorator classes, each handling a specific aspect of functionality.

## Can I combine this design pattern with others? Which ones?

The Decorator pattern can be effectively combined with several other design patterns:

- Adapter: Decorator can change the interface of an object while Adapter makes incompatible objects work together
- Bridge: Both patterns can be used to change behavior dynamically
Composite: Decorator can be viewed as a degenerate Composite with only one component
- Strategy: Decorator alters the object's skin while Strategy changes the guts
- Chain of Responsibility: Decorators can extend object's behavior while maintaining the same interface
- Factory Method: Can be used to create decorators dynamically

## Contents of this section

The implementation in `main.py` demonstrates the Decorator pattern through a data handling system with the following components:

### Component Interface:
- `DataSource`: Abstract interface defining core operations
  - `write_data(data)`: Writes data to source
  - `read_data()`: Reads data from source

### Concrete Component:
- `FileDataSource`: Basic implementation working with files
  - Implements actual file reading/writing operations
  - Stores filename and manages file operations

### Base Decorator:
- `DataSourceDecorator`: Abstract base for all decorators
  - Implements component interface
  - Holds reference to wrapped component
  - Delegates operations to wrapped component

### Concrete Decorators:
- `EncryptionDecorator`: Adds encryption/decryption functionality
  - Encrypts data before writing
  - Decrypts data after reading

- `CompressionDecorator`: Adds compression functionality
  - Compresses data before writing
  - Decompresses data after reading

### Client Code:
- `Application`: Demonstrates decorator usage
  - Shows how decorators can be stacked
  - Illustrates dynamic addition of behaviors

## License

This work is licensed under CC BY-NC-SA 4.0. See the LICENSE.md file for details.