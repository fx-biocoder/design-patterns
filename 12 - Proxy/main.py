"""
Proxy Pattern - Design Patterns (GoF)

Author: Facundo Martínez (fx-biocoder)
Repository: https://github.com/fx-biocoder/design-patterns

Description:
This file contains an implementation for the Proxy design pattern, one of the 23 design patterns described
by the Gang of Four (GoF). This pattern allows for providing a substitute or position marker to another object.
This code is based on the concepts and examples presented in the book "Dive Into Design Patterns" by Alexey Naumov.

Components:
- ThirdPartyYoutubeLib: The service interface
- CachedYoutubeClass: Proxy that points at a service object (i.e., the service interface)
- ThirdPartYoutubeClass: The service that provides the business logic

License:
CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/deed.en)
"""
from abc import ABC, abstractmethod


class ThirdPartyYoutubeLib(ABC):
    @abstractmethod
    def list_videos(self):
        raise NotImplementedError

    @abstractmethod
    def get_video_info(self, _id: int=None):
        raise NotImplementedError

    @abstractmethod
    def download_video(self, _id: int=None):
        raise NotImplementedError


class CachedYoutubeClass(ThirdPartyYoutubeLib):
    def __init__(self, service: ThirdPartyYoutubeLib):
        self._service = service
        self._list_cache = []
        self._video_cache = []

    def list_videos(self):
        pass

    def get_video_info(self, _id: int=None):
        pass

    def download_video(self, _id: int=None):
        pass


class ThirdPartyYoutubeClass(ThirdPartyYoutubeLib):
    def list_videos(self):
        pass

    def get_video_info(self, _id: int=None):
        pass

    def download_video(self, _id: int=None):
        pass


class YoutubeManager:
    def __init__(self, service: ThirdPartyYoutubeLib):
        self._service = service

    def render_video_page(self, _id):
        info = self._service.get_video_info(_id)
        return info

    def render_list_panel(self):
        videos_list = self._service.list_videos()
        return videos_list

    def react_on_user_input(self, _id=None) -> None:
        self.render_video_page(_id)
        self.render_list_panel()


class Application:
    def __init__(self):
        youtube_service = ThirdPartyYoutubeClass()
        youtube_proxy = CachedYoutubeClass(youtube_service)
        manager = YoutubeManager(youtube_proxy)
        manager.react_on_user_input()


if __name__ == "__main__":
    app = Application()
