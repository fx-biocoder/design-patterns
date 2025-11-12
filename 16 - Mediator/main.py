"""
Mediator Pattern - Design Patterns (GoF)

Author: Facundo Martínez (fx-biocoder)
Repository: https://github.com/fx-biocoder/design-patterns

Description:
This file contains an implementation for the Mediator design pattern, one of the 23 design patterns described by the
Gang of Four (GoF). This pattern allows for reducing dependencies between objects. The pattern restricts direct
communications between objects, forcing them to collaborate only through a mediator object.
This code is based on the concepts and examples presented in the book "Dive Into Design Patterns" by Alexey Naumov.

Components:
- Mediator: Abstract interface defining the method to notify components about events and handle their interactions.
- Component: Base class for components that communicate through the mediator instead of directly with each other.
- Button: Concrete component representing a clickable button that notifies the mediator of click events.
- Checkbox: Concrete component representing a checkbox that can notify the mediator of check events.
- TextBox: Concrete component representing a text input field that can notify the mediator of keypress events.
- AuthenticationDialog: Concrete mediator that manages interactions between UI components in an authentication dialog.

License:
CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/deed.en)
"""
from abc import ABC, abstractmethod


class Mediator(ABC):
    @abstractmethod
    def notify(self, sender: 'Component', event: str):
        raise NotImplementedError

class Component:
    def __init__(self, dialog: Mediator):
        self.dialog: Mediator = dialog

    def click(self) -> None:
        self.dialog.notify(self, 'click')

    def keypress(self) -> None:
        self.dialog.notify(self, 'keypress')


class Button(Component):
    def __init__(self, mediator: Mediator):
        super().__init__(mediator)


class Checkbox(Component):
    def __init__(self, mediator: Mediator):
        super().__init__(mediator)

    def check(self) -> None:
        self.dialog.notify(self, 'check')


class TextBox(Component):
    def __init__(self, mediator: Mediator):
        super().__init__(mediator)


class AuthenticationDialog(Mediator):
    def __init__(self):
        """
        The constructor creates all component objects and passes the current mediator
        to their constructors to link them
        """
        self.title: str = ""
        self.login_or_register: bool = False
        self.login_username: str = ""
        self.login_password: str = ""
        self.reg_username: str = ""
        self.reg_password: str = ""
        self.reg_email: str = ""
        self.ok: Button = Button(self)
        self.cancel: Button = Button(self)
        self.remember_me: Checkbox = Checkbox(self)

    def notify(self, sender: Component, event: str):
        pass



