# Command design pattern

## Description

The Command pattern is a behavioral design pattern that encapsulates a request as an object, thereby letting you parameterize clients with queues, requests, and support undoable operations. Commands decouple the object that invokes the operation from the one that knows how to perform it.

## What specific problems do I solve using this pattern?

The Command pattern addresses problems where you need to represent actions as objects. It enables queuing, logging, and undo/redo operations, and lets you parameterize objects with operations. The pattern also simplifies the addition of new commands without changing existing code.

## Can I combine this design pattern with others? Which ones?

The Command pattern can be combined with several other patterns:

- Composite: Commands can be composed into macro commands that execute multiple actions
- Memento: Commands can integrate Memento to capture object state for precise undo
- Invoker/Receiver structure: Command works with invokers that call commands and receivers that perform the action
- Factory Method: Use factories to create command instances dynamically
- Chain of Responsibility: Commands can be passed through a chain for pre-processing or handling

## Contents of this section

The implementation in `main.py` demonstrates the Command pattern through a text editor example with the following components:

`Command`: Abstract base class that holds references to the `Application` and `Editor` and provides `save_backup()` and `undo()` helpers. Concrete commands implement `execute()` and return a boolean indicating whether the command should be pushed onto history.

`CopyCommand`: Copies the current selection from the editor to the application's clipboard. Returns False because it does not modify the editor state.

`CutCommand`: Saves a backup, copies the selection to the clipboard, deletes the selection from the editor, and returns True so it can be undone.

`PasteCommand`: Saves a backup, replaces the selection with the clipboard contents, and returns True for undo support.

`UndoCommand`: Calls the application's undo method and returns False.

`CommandHistory`: Simple stack storing executed commands for undo functionality.

`Editor`: Mock editor class with placeholder methods `get_selection()`, `delete_selection()`, and `replace_selection()` which print debug messages in this example.

`Application`: Manages clipboard, editors, and command history. Provides `execute_command()` and `undo()` helpers and a `create_ui()` method that returns a mapping of UI actions to command invocations.

## License

This work is licensed under CC BY-NC-SA 4.0. See the LICENSE.md file for details.