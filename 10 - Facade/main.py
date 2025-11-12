"""
Facade Pattern - Design Patterns (GoF)

Author: Facundo Martínez (fx-biocoder)
Repository: https://github.com/fx-biocoder/design-patterns

Description:
This file contains an implementation for the Facade design pattern, one of the 23 design patterns described
by the Gang of Four (GoF). This pattern allows for providing a simplified interface to a library, a framework, or any
other complex group of classes.
This code is based on the concepts and examples presented in the book "Dive Into Design Patterns" by Alexey Naumov.

Components:
- VideoConverter: The facade that encapsulates the functionality of a complex video conversion framework
- File: A generic class for files
- VideoFile: A generic class for video files
- Framework Dependencies: OggCompressionCodec, MPEG4CompressionCodec, CodecFactory, BitrateReader, AudioMixer
- Application: The app that runs the framework

License:
CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/deed.en)
"""
class File:
    def __init__(self, filename):
        self.filename = filename

    @staticmethod
    def save() -> None:
        print("Saving file...")


class VideoFile:
    def __init__(self, filename):
        self.filename = filename


class OggCompressionCodec:
    pass


class MPEG4CompressionCodec:
    pass


class CodecFactory:
    @staticmethod
    def extract(file):
        return "file format"


class BitrateReader:
    @staticmethod
    def read(file, source_codec):
        return f"Reading {file} with codec: {source_codec}..."

    @staticmethod
    def convert(buffer, destination_codec):
        return f"Buffer converted from {buffer} to {destination_codec}"

class AudioMixer:
    @staticmethod
    def convert(buffer, destination_codec):
        return f"Converting from {buffer} to {destination_codec}"

    @staticmethod
    def fix(result):
        return f"Fixing result to {result}"


class VideoConverter:
    @staticmethod
    def convert(filename, _format):
        file = VideoFile(filename)
        source_codec = CodecFactory.extract(file)

        if _format == "mp4":
            destination_codec = MPEG4CompressionCodec()
        else:
            destination_codec = OggCompressionCodec()

        buffer = BitrateReader.read(file, source_codec)
        result = BitrateReader.convert(buffer, destination_codec)
        result = AudioMixer().fix(result)
        return File(result)


class Application:
    @staticmethod
    def main():
        convertor = VideoConverter()
        mp4 = convertor.convert("file.dat", "mp4")
        mp4.save()


if __name__ == "__main__":
    Application().main()
