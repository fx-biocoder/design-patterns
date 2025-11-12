"""
Iterator Pattern - Design Patterns (GoF)

Author: Facundo Martínez (fx-biocoder)
Repository: https://github.com/fx-biocoder/design-patterns

Description:
This file contains an implementation for the Iterator design pattern, one of the 23 design patterns described by the Gang
of Four (GoF). This pattern allows for iterating through elements of a collection without exposing their subjacent
representation (e.g., list, stack, tree, etcetera).
This code is based on the concepts and examples presented in the book "Dive Into Design Patterns" by Alexey Naumov.

Components:
- Profile: Represents a user profile with identifier and email information that can be iterated over.
- ProfileIterator: Abstract interface defining methods to iterate through profile collections.
- SocialNetwork: Abstract interface for creating iterators specific to different relationship types.
- FacebookIterator: Concrete iterator implementation that traverses Facebook profiles with lazy initialization.
- SocialSpammer: Client class that uses iterators to send messages to profile collections without accessing them directly.
- Facebook: Concrete social network that creates FacebookIterator instances for different relationship types.
- LinkedIn: Another concrete social network implementation example for reference.
- Application: Client application.

License:
CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/deed.en)
"""
from abc import ABC, abstractmethod
from typing import List, Any


class Profile:
    def __init__(self, profile_id: str, email: str):
        self.profile_id = profile_id
        self.email = email

    def get_id(self) -> str:
        return self.profile_id

    def get_email(self) -> str:
        return self.email


class ProfileIterator(ABC):
    @abstractmethod
    def get_next(self) -> Profile:
        raise NotImplementedError

    @abstractmethod
    def has_more(self) -> bool:
        raise NotImplementedError


class SocialNetwork(ABC):
    @abstractmethod
    def create_friends_iterator(self, profile_id) -> ProfileIterator:
        raise NotImplementedError

    @abstractmethod
    def create_coworkers_iterator(self, profile_id) -> ProfileIterator:
        raise NotImplementedError


class FacebookIterator(ProfileIterator):
    def __init__(self, facebook: 'Facebook', profile_id: str, _type: str):
        self._facebook = facebook
        self._profile_id = profile_id
        self._type = _type
        self._current_position: int = 0
        self._cache: List[Profile] = []

    def _lazy_init(self):
        if not self._cache:
            self._cache = self._facebook.social_graph_request(self._profile_id, self._type)

    def has_more(self) -> bool:
        self._lazy_init()
        return self._current_position < len(self._cache)

    def get_next(self) -> Profile | None:
        if self.has_more():
            result = self._cache[self._current_position]
            self._current_position += 1
            return result


class SocialSpammer:
    """
    You can pass an iterator to a client class instead of giving access to a complete collection, to avoid exposing
    the collection to the client. Another advantage is that you can change the way in which the client works with the
    collection during runtime by passing a different iterator.
    """
    @staticmethod
    def _send_email(email: str, message: str):
        print(f"Sending {message} to {email}")

    def send(self, iterator: ProfileIterator, message: str):
        while iterator.has_more():
            profile = iterator.get_next()
            self._send_email(profile.get_email(), message)


class Facebook(SocialNetwork):
    def create_friends_iterator(self, profile_id) -> ProfileIterator:
        return FacebookIterator(self, profile_id, "friends")

    def create_coworkers_iterator(self, profile_id) -> ProfileIterator:
        return FacebookIterator(self, profile_id, "coworkers")

    def social_graph_request(self, _profile_id, _type):
        # Returns a list of profiles
        pass

class LinkedIn(SocialNetwork):
    """Just another example of a social network to work with"""
    def create_friends_iterator(self, profile_id) -> ProfileIterator:
        pass

    def create_coworkers_iterator(self, profile_id) -> ProfileIterator:
        pass

    def social_graph_request(self, _profile_id, _type):
        pass


class Application:
    def __init__(self):
        self.network: SocialNetwork | None = None
        self.spammer: SocialSpammer | None = None

    def config(self):
        network: Any = None

        # Setting up network depending on which network you are working with
        match network:
            case "Facebook":
                self.network = Facebook()
            case "LinkedIn":
                self.network = LinkedIn()

        self.spammer = SocialSpammer()

    def send_spam_to_friends(self, profile):
        iterator = self.network.create_friends_iterator(profile.get_id())
        self.spammer.send(iterator, "Hello, I am a Nigerian prince, and I want to share my wealth with you!!!")

    def send_spam_to_coworkers(self, profile):
        iterator = self.network.create_coworkers_iterator(profile.get_id())
        self.spammer.send(iterator, "Meetings Meetings Meetings Meetings!!!")










