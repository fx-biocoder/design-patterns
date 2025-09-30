"""
Singleton Pattern - Design Patterns (GoF)

Author: Facundo Martínez (fx-biocoder)
Repository: https://github.com/fx-biocoder/design-patterns

Description:
This file contains an implementation for the Singleton design pattern, one of the 23 design patterns described
by the Gang of Four (GoF). 
This code is based on the concepts and examples presented in the book "Dive Into Design Patterns" by Alexey Naumov.

Components:
- SingletonMeta: A metaclass that implements the singleton behavior
- MyClass: An example class using the singleton metaclass
- OtherClass: Another example class using the singleton metaclass

License:
CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/deed.en)
"""
import threading


# Inspired in https://stackoverflow.com/questions/6760685/what-is-the-best-way-of-implementing-a-singleton-in-python
class SingletonMeta(type):
    _instances: dict[type, object] = {}
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances: 
                cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)

        return cls._instances[cls]


class MyClass(metaclass=SingletonMeta):
    pass


class OtherClass(metaclass=SingletonMeta):
    pass


def main():
    obj = MyClass()
    print(obj)
    other_obj = OtherClass()
    print(other_obj)


if __name__ == '__main__':
    main()
