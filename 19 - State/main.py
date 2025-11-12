"""
State Pattern - Design Patterns (GoF)

Author: Facundo Martínez (fx-biocoder)
Repository: https://github.com/fx-biocoder/design-patterns

Description:
This file contains an implementation for the State design pattern, one of the 23 design patterns described by the
Gang of Four (GoF). This pattern allows for altering the behavior of an object when its internal state changes.
This code is based on the concepts and examples presented in the book "Dive Into Design Patterns" by Alexey Naumov.

Components:
- State: Abstract base class defining the interface for different states that an audio player can be in.
- ReadyState: Concrete state representing a player that is ready to play or perform navigation operations.
- LockedState: Concrete state representing a locked player that cannot play, skip, or navigate through songs.
- PlayingState: Concrete state representing a player that is currently playing audio content.
- UserInterface: Provides UI controls that delegate user actions to the current state of the audio player.
- AudioPlayer: Context class that maintains the current state and delegates behavior based on that state.

License:
CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/deed.en)
"""
from abc import ABC, abstractmethod


class State(ABC):
    def __init__(self, player: 'AudioPlayer'):
        self.player = player

    @abstractmethod
    def click_lock(self):
        raise NotImplementedError

    @abstractmethod
    def click_play(self):
        raise NotImplementedError

    @abstractmethod
    def click_next(self):
        raise NotImplementedError

    @abstractmethod
    def click_previous(self):
        raise NotImplementedError


class ReadyState(State):
    def click_lock(self) -> None:
        self.player.change_state(LockedState(self.player))

    def click_play(self) -> None:
        self.player.start_playback()
        self.player.change_state(PlayingState(self.player))

    def click_next(self) -> None:
        self.player.next_song()

    def click_previous(self) -> None:
        self.player.previous_song()


class LockedState(State):
    def click_lock(self) -> None:
        if self.player.state.__class__ == PlayingState:
            self.player.change_state(PlayingState(self.player))
        else:
            self.player.change_state(ReadyState(self.player))

    def click_play(self):
        # Does not follow Interface Segregation Principle...
        pass

    def click_next(self):
        # Does not follow Interface Segregation Principle...
        pass

    def click_previous(self):
        # Does not follow Interface Segregation Principle...
        pass


class PlayingState(State):
    def click_lock(self) -> None:
        self.player.change_state(LockedState(self.player))

    def click_play(self) -> None:
        self.player.stop_playback()
        self.player.change_state(ReadyState(self.player))

    def click_next(self) -> None:
        self.player.next_song()

    def click_previous(self) -> None:
        self.player.previous_song()


class UserInterface:
    def __init__(self, player: 'AudioPlayer'):
        self.player = player

    def click_lock(self) -> None:
        self.player.click_lock()

    def click_play(self) -> None:
        self.player.click_play()

    def click_next(self) -> None:
        self.player.click_next()

    def click_previous(self) -> None:
        self.player.click_previous()


class AudioPlayer:
    def __init__(self):
        self.state = ReadyState(self)
        self.ui = UserInterface(self)

    def change_state(self, state) -> None:
        self.state = state

    def click_lock(self) -> None:
        self.state.click_lock()

    def click_play(self) -> None:
        self.state.click_play()

    def click_next(self) -> None:
        self.state.click_next()

    def click_previous(self) -> None:
        self.state.click_previous()

    @staticmethod
    def start_playback() -> None:
        print("Started playback")

    @staticmethod
    def stop_playback() -> None:
        print("Stopped playback")

    @staticmethod
    def next_song() -> None:
        print("Next song")

    @staticmethod
    def previous_song() -> None:
        print("Previous song")

    @staticmethod
    def fast_forward(time: int) -> None:
        print(f"Fast forward: {time} seconds")

    @staticmethod
    def rewind(time: int) -> None:
        print(f"Rewind: {time} seconds")
