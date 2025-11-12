"""
Memento Pattern - Design Patterns (GoF)

Author: Facundo Martínez (fx-biocoder)
Repository: https://github.com/fx-biocoder/design-patterns

Description:
This file contains an implementation for the Memento design pattern, one of the 23 design patterns described by the
Gang of Four (GoF). This pattern allows for reducing dependencies between objects. The pattern allows for saving and
restoring the previous state of an object without revealing implementation details.
This code is based on the concepts and examples presented in the book "Dive Into Design Patterns" by Alexey Naumov.

Components:
- Snapshot: Encapsulates the state of an Editor at a particular moment.
- Editor: Originator class that maintains its internal state and creates snapshots of it.
- Command: Caretaker class that manages memento backups.

License:
CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/deed.en)
"""
class Snapshot:
    def __init__(self,
                 editor: 'Editor',
                 text: str,
                 cursor: dict[str, int],
                 selection_width: int):
        self._editor = editor
        self._text = text
        self._cursor = cursor
        self._selection_width = selection_width

    def restore(self):
        self._editor.text = self._text
        self._editor.cursor = self._cursor
        self._editor.selection_width = self._selection_width


class Editor:
    def __init__(self):
        self._text: str = ""
        self._cursor: dict[str, int] = {'x': 0, 'y': 0}
        self._selection_width: int = 0

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text):
        self._text = text

    @property
    def cursor(self):
        return self._cursor

    @cursor.setter
    def cursor(self, *values):
        self._cursor['x'] = values[0]
        self._cursor['y'] = values[1]

    @property
    def selection_width(self):
        return self._selection_width

    @selection_width.setter
    def selection_width(self, width: int):
        self._selection_width = width

    def create_snapshot(self):
        return Snapshot(
            self,
            self.text,
            self.cursor,
            self.selection_width,
        )


class Command:
    def __init__(self):
        self._backup: Snapshot | None = None

    def make_backup(self, editor: Editor):
        self._backup = editor.create_snapshot()

    def undo(self):
        if self._backup:
            self._backup.restore()
