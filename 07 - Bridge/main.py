"""
Bridge Pattern - Design Patterns (GoF)

Author: Facundo Martínez (fx-biocoder)
Repository: https://github.com/fx-biocoder/design-patterns

Description:
This file contains an implementation for the Bridge design pattern, one of the 23 design patterns described
by the Gang of Four (GoF). This pattern allows for dividing a large class, or a group of closely linked classes, into
two separated hierarchies (i.e., abstraction and implementation) that can be developed independently of one another.
This code is based on the concepts and examples presented in the book "Dive Into Design Patterns" by Alexey Naumov.

Components:
- Remote: An abstraction
- Device: An implementation
- AdvancedRemote: A concrete abstraction
- Televisor: A concrete implementation
- Radio: Another concrete implementation


License:
CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/deed.en)
"""
from abc import ABC, abstractmethod


class Device(ABC):
    @abstractmethod
    def is_enabled(self):
        raise NotImplementedError

    @abstractmethod
    def enable(self):
        raise NotImplementedError

    @abstractmethod
    def disable(self):
        raise NotImplementedError

    @abstractmethod
    def get_volume(self):
        raise NotImplementedError

    @abstractmethod
    def set_volume(self, percent: int):
        raise NotImplementedError

    @abstractmethod
    def get_channel(self):
        raise NotImplementedError

    @abstractmethod
    def set_channel(self, channel: int):
        raise NotImplementedError


class RemoteControl(ABC):
    def __init__(self, device: Device):
        self._device = device

    def toggle_power(self) -> None:
        if self._device.is_enabled():
            self._device.disable()
        else:
            self._device.enable()

    def volume_down(self) -> None:
        self._device.set_volume(self._device.get_volume() - 10)

    def volume_up(self) -> None:
        self._device.set_volume(self._device.get_volume() + 10)

    def channel_down(self) -> None:
        self._device.set_channel(self._device.get_channel() - 1)

    def channel_up(self) -> None:
        self._device.set_channel(self._device.get_channel() + 1)


class AdvancedRemoteControl(RemoteControl):
    def __init__(self, device: Device):
        super().__init__(device)

    def mute(self) -> None:
        self._device.set_volume(0)


class Televisor(Device):
    def is_enabled(self):
        pass

    def enable(self):
        pass

    def disable(self):
        pass

    def get_volume(self):
        pass

    def set_volume(self, percent: int):
        pass

    def get_channel(self):
        pass

    def set_channel(self, channel: int):
        pass


class Radio(Device):
    def is_enabled(self):
        pass

    def enable(self):
        pass

    def disable(self):
        pass

    def get_volume(self):
        pass

    def set_volume(self, percent: int):
        pass

    def get_channel(self):
        pass

    def set_channel(self, channel: int):
        pass


def client() -> None:
    tv = Televisor()
    remote = RemoteControl(tv)
    remote.toggle_power()

    radio = Radio()
    other_remote = AdvancedRemoteControl(radio)
    other_remote.mute()


if __name__ == '__main__':
    client()
