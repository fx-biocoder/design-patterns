"""
Command Pattern - Design Patterns (GoF)

Author: Facundo Martínez (fx-biocoder)
Repository: https://github.com/fx-biocoder/design-patterns

Description:
This file contains an implementation for the Command design pattern, one of the 23 design patterns described by the Gang
of Four (GoF). This pattern allows for converting a request into an independent object that contains all the information
about the request.
This code is based on the concepts and examples presented in the book "Dive Into Design Patterns" by Alexey Naumov.

Components:
- Command: Base class for defining the common interface for all concrete commands
- CopyCommand, CutCommand, PasteCommand, UndoCommand: Concrete commands
- CommandHistory: Stack that contains all called commands
- Editor: Class for mocking text editing operations.
- Application: Creates command objects and executes them

License:
CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/deed.en)
"""
from abc import ABC, abstractmethod
from typing import List, Dict, Callable


class Command(ABC):
    def __init__(self, app: 'Application'=None, editor: 'Editor'=None):
        self._app: 'Application' = app
        self._editor: 'Editor' = editor
        self._backup: str = ""

    def save_backup(self):
        self._backup: str = self._editor.text

    def undo(self) -> None:
        self._editor.text = self._backup

    @abstractmethod
    def execute(self):
        raise NotImplementedError


class CopyCommand(Command):
    def __init__(self, app: 'Application', editor: 'Editor'):
        super().__init__(app, editor)

    def execute(self) -> bool:
        self._app.clipboard = self._editor.get_selection()
        return False


class CutCommand(Command):
    def __init__(self, app: 'Application', editor: 'Editor'):
        super().__init__(app, editor)

    def execute(self) -> bool:
        self.save_backup()
        self._app.clipboard = self._editor.get_selection()
        self._editor.delete_selection()
        return True


class PasteCommand(Command):
    def __init__(self, app: 'Application', editor: 'Editor'):
        super().__init__(app, editor)

    def execute(self) -> bool:
        self.save_backup()
        self._editor.replace_selection(self._app.clipboard)
        return True


class UndoCommand(Command):
    def __init__(self, app: 'Application', editor: 'Editor'):
        super().__init__(app, editor)

    def execute(self) -> bool:
        self._app.undo()
        return False


class CommandHistory:
    def __init__(self):
        self._history: List[Command] = []

    def push(self, command: Command) -> None:
        self._history.append(command)

    def pop(self) -> Command:
        return self._history.pop()


class Editor:
    def __init__(self):
        self.text: str = ""

    @staticmethod
    def get_selection() -> str:
        # Should return the selected text
        print("Editor.get_selection() called")
        return ""

    @staticmethod
    def delete_selection() -> None:
        # Should delete the selected text
        print("Editor.delete_selection() called")

    @staticmethod
    def replace_selection(text: str) -> None:
        # Should insert the clipboard contents into the current position
        print(f"Replacing selection with {text}...")


class Application:
    def __init__(self):
        self.clipboard = ""
        self.editors = [Editor()]
        self.active_editor = self.editors[0]
        self.history = CommandHistory()

    def execute_command(self, command: Command) -> None:
        if command.execute():
            self.history.push(command)

    def undo(self) -> None:
        command = self.history.pop()
        if command:
            command.undo()

    def create_ui(self) -> Dict[str, Callable]:
        # Code for creating the UI goes here...
        copy = lambda: self.execute_command(CopyCommand(self, self.active_editor))
        cut = lambda: self.execute_command(CutCommand(self, self.active_editor))
        paste = lambda: self.execute_command(PasteCommand(self, self.active_editor))
        undo = lambda: self.execute_command(UndoCommand(self, self.active_editor))

        return {
            "copy": copy,
            "cut": cut,
            "paste": paste,
            "undo": undo
        }


if __name__ == "__main__":
    my_app = Application()
    my_app.create_ui()
