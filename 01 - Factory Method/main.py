"""
Factory Method Pattern - Design Patterns (GoF)

Author: Facundo Martínez (fx-biocoder)
Repository:

Description:
This file contains an implementation for the Factory Method design pattern, one of the 23 design patterns described
by the Gang of Four (GoF). This pattern allows for defining an interface to create objects in a superclass, while
allowing subclasses to alter the type of object being created. This code is based on the concepts and examples presented
in the book "Dive Into Design Patterns" by Alexey Naumov.

License:
CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/deed.en)
"""

from abc import ABC, abstractmethod


class Button(ABC):
    """Common interface for buttons"""
    @abstractmethod
    def on_click(self):
        pass

    @abstractmethod
    def render(self):
        pass


class WindowsButton(Button):
    """Implementation of a Windows button"""
    def on_click(self) -> None:
        print("Windows button clicked")

    def render(self) -> None:
        print("Windows button rendered")


class HTMLButton(Button):
    """Implementation of an HTML button"""
    def on_click(self) -> None:
        print("HTML button clicked")

    def render(self) -> None:
        print("HTML button rendered")


class Dialog(ABC):
    """Abstract base class for dialogs"""
    def render(self) -> None:
        button = self.create_button()
        button.render()
        button.on_click()

    @abstractmethod
    def create_button(self):
        pass


class WindowsDialog(Dialog):
    """Child class for Windows dialogs"""
    def create_button(self) -> WindowsButton:
        return WindowsButton()


class WebDialog(Dialog):
    """Child class for Web dialogs"""
    def create_button(self) -> HTMLButton:
        return HTMLButton()


def render_dialog(dialog: Dialog) -> None:
    """Helper function for rendering dialogs"""
    dialog.render()


if __name__ == "__main__":
    render_dialog(WebDialog())
    render_dialog(WindowsDialog())
