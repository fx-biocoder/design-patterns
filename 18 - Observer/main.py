"""
Observer Pattern - Design Patterns (GoF)

Author: Facundo Martínez (fx-biocoder)
Repository: https://github.com/fx-biocoder/design-patterns

Description:
This file contains an implementation for the Observer design pattern, one of the 23 design patterns described by the
Gang of Four (GoF). This pattern allows for defining a subscription mechanism to notify several objects about any event
that happens to the observed object.
This code is based on the concepts and examples presented in the book "Dive Into Design Patterns" by Alexey Naumov.

Components:
- EventListeners: Abstract interface defining the update method that observers must implement.
- EmailAlertsListener: Concrete observer that sends email notifications when events occur.
- LoggingListener: Concrete observer that logs events to a file when notifications are received.
- EventManager: Manages the subscription and notification of multiple listeners.
- Editor: Concrete subject that maintains file operations and notifies registered listeners.

License:
CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/deed.en)
"""
from abc import ABC, abstractmethod
from typing import List, IO, AnyStr


class EventListeners(ABC):
    @abstractmethod
    def update(self, filename):
        raise NotImplementedError


class EmailAlertsListener(EventListeners):
    def __init__(self, email, message):
        self._email = email
        self._message = message

    def update(self, filename):
        # Should email the specified email address
        pass


class LoggingListener(EventListeners):
    def __init__(self, log_filename, message):
        self._log = log_filename
        self._message = message

    def update(self, filename):
        with open(self._log, 'a') as file:
            file.write(f"File: {filename}, message: {self._message}\n")


class EventManager:
    def __init__(self):
        self._listeners: dict[str, List[EventListeners]] = dict()

    def subscribe(self, event_type, listener):
        self._listeners[event_type].append(listener)

    def unsubscribe(self, event_type, listener):
        self._listeners[event_type].remove(listener)

    def notify(self, event_type, data):
        for listener in self._listeners[event_type]:
            listener.update(data)


class Editor:
    def __init__(self):
        self.events: EventManager = EventManager()
        self.file: IO[AnyStr] | None = None

    def open_file(self):
        self.file = open("file.dat")  # Might not be the most optimal way, but for illustrative purposes it's fine
        self.events.notify('open', self.file.name)

    def save_file(self):
        self.file.write(self.file.name)
        self.events.notify('save', self.file.name)
