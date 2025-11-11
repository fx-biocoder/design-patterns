"""
Decorator Pattern - Design Patterns (GoF)

Author: Facundo Martínez (fx-biocoder)
Repository: https://github.com/fx-biocoder/design-patterns

Description:
This file contains an implementation for the Decorator design pattern, one of the 23 design patterns described
by the Gang of Four (GoF). This pattern allows for adding functionalities to objects by placing them inside special
wrapper objects that contain these functionalities.
This code is based on the concepts and examples presented in the book "Dive Into Design Patterns" by Alexey Naumov.

Components:
- DataSource: Interface
- FileDataSource
- DataSourceDecorator
- EncryptionDecorator
- CompressionDecorator


License:
CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/deed.en)
"""
from abc import ABC, abstractmethod


class DataSource(ABC):
    @abstractmethod
    def write_data(self, data):
        raise NotImplementedError()

    @abstractmethod
    def read_data(self):
        raise NotImplementedError()


class FileDataSource(DataSource):
    def __init__(self, filename):
        self._filename = filename

    def write_data(self, data):
        with open(self._filename, 'w') as f:
            f.write(data)

    def read_data(self):
        with open(self._filename, 'r') as f:
            return f.read()


class DataSourceDecorator(DataSource):
    def __init__(self, source: DataSource):
        self._wrapped = source

    def write_data(self, data):
        self._wrapped.write_data(data)

    def read_data(self):
        return self._wrapped.read_data()


class EncryptionDecorator(DataSourceDecorator):
    def __init__(self, source: DataSource):
        super().__init__(source)

    def write_data(self, data):
        # Performs encryption here
        self._wrapped.write_data(data)

    def read_data(self):
        data = self._wrapped.read_data()
        # Decrypts data and then returns it
        return data


class CompressionDecorator(DataSourceDecorator):
    def __init__(self, source: DataSource):
        super().__init__(source)

    def write_data(self, data):
        # Compresses data and then writes it
        self._wrapped.write_data(data)

    def read_data(self):
        data = self._wrapped.read_data()
        # Decompresses data if compressed, and then returns it
        return data


class Application:
    @staticmethod
    def usage_example():
        source = FileDataSource("file.dat")
        source.write_data("test")

        source = CompressionDecorator(source)
        source.write_data("another test")

        source = EncryptionDecorator(source)
        source.write_data("yet another test")


if __name__ == "__main__":
    app = Application()
    app.usage_example()
