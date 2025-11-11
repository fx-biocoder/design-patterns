"""
Chain of Responsibility Pattern - Design Patterns (GoF)

Author: Facundo Martínez (fx-biocoder)
Repository: https://github.com/fx-biocoder/design-patterns

Description:
This file contains an implementation for the Chain of Responsibility design pattern, one of the 23 design patterns
described by the Gang of Four (GoF). This pattern allows for passing requests through a chain of handlers, where each
handler decides if it processes the request or passes it to the next handler.
This code is based on the concepts and examples presented in the book "Dive Into Design Patterns" by Alexey Naumov.

Components:
- ComponentWithContextualHelp: Interface for handlers
- Component: Base class for simple components
- Container: Class for storing simple components or child containers
- UI elements (Dialog, Panel, Button)
- Application: Mock user application

License:
CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/deed.en)
"""
from abc import ABC, abstractmethod
from typing import List, Optional


class ComponentWithContextualHelp(ABC):
    @abstractmethod
    def show_help(self):
        raise NotImplementedError


class Component(ComponentWithContextualHelp):
    def __init__(self, tooltip_text=None):
        self._container: Optional['Container'] = None
        self.tooltip_text = tooltip_text

    def show_help(self) -> None:
        if self.tooltip_text:
            print(self.tooltip_text)
        elif self._container:
            self._container.show_help()
        else:
            print("No tips available.")


class Container(Component):
    def __init__(self, tooltip_text: Optional[str] = None):
        super().__init__(tooltip_text)
        self._children: List[Component] = []

    def add(self, child: Component) -> None:
        self._children.append(child)
        child.container = self


class Button(Component):
    pass


class Panel(Container):
    def __init__(self, modal_help_text: Optional[str] = None):
        super().__init__()
        self._modal_help_text = modal_help_text

    def show_help(self) -> None:
        if self._modal_help_text:
            print(self._modal_help_text)
        else:
            super().show_help()


class Dialog(Container):
    def __init__(self, title: str, wiki_page_url: Optional[str] = None):
        super().__init__()
        self._title = title
        self._wiki_page_url = wiki_page_url

    def show_help(self) -> None:
        if self._wiki_page_url:
            print(self._wiki_page_url)
        else:
            super().show_help()


class Application:
    def __init__(self):
        self.dialog: Optional[Dialog] = None
        self.ok_button: Optional[Button] = None
        self.cancel_button: Optional[Button] = None
        self.panel: Optional[Panel] = None

    def create_ui(self) -> None:
        dialog = Dialog("Budget Reports", "https://example.com")
        panel = Panel("Panel for budget reports")
        ok = Button("OK button")
        ok.tooltip_text = "This is the OK button that confirms the action"
        cancel = Button("Cancel button")
        cancel.tooltip_text = "This button cancels the current operation"

        panel.add(ok)
        panel.add(cancel)
        dialog.add(panel)

        self.dialog = dialog
        self.ok_button = ok
        self.cancel_button = cancel
        self.panel = panel

    @staticmethod
    def on_f1_key_press(component: Component) -> None:
        component.show_help()


if __name__ == '__main__':
    app = Application()
    app.create_ui()

    # Get help tips
    app.on_f1_key_press(app.ok_button)
    app.on_f1_key_press(app.panel)
    app.on_f1_key_press(app.dialog)
