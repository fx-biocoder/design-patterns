"""
This code needs to be revised.
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
