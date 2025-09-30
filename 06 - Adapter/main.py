"""
Adapter Pattern - Design Patterns (GoF)

Author: Facundo Martínez (fx-biocoder)
Repository: https://github.com/fx-biocoder/design-patterns

Description:
This file contains an implementation for the Adapter design pattern, one of the 23 design patterns described
by the Gang of Four (GoF). This pattern allows for delegating the cloning process to the objects that are being cloned
instead of manually creating exact copies.
This code is based on the concepts and examples presented in the book "Dive Into Design Patterns" by Alexey Naumov.

Components:
- RoundPeg: A class defining a round peg
- RoundHole: A class defining a round hole
- SquarePeg: A class defining a square peg, which is not compatible with round holes.
- SquarePegAdapter: A class defining a square peg adapter to fit into round holes.


License:
CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/deed.en)
"""
import math


class RoundPeg:
    def __init__(self, radius: int):
        self.radius = radius

    def get_radius(self):
        return self.radius


class RoundHole:
    def __init__(self, radius: int):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def fits(self, peg: RoundPeg):
        return self.get_radius() >= peg.get_radius()


class SquarePeg:
    def __init__(self, width: int):
        self.width = width

    def get_width(self):
        return self.width


class SquarePegAdapter(RoundPeg):
    def __init__(self, peg: SquarePeg, radius: int):
        super().__init__(radius)
        self.peg = peg

    def get_radius(self):
        return self.peg.get_width() * math.sqrt(2) / 2


def client():
    hole = RoundHole(radius=5)
    round_peg = RoundPeg(radius=5)
    hole.fits(round_peg) # True

    small_square_peg = SquarePeg(width=5)
    large_square_peg = SquarePeg(width=10)
    # hole.fits(small_square_peg)  # Incompatible, square pegs do not fit into round holes

    small_square_peg_adapter = SquarePegAdapter(peg=small_square_peg, radius=5)
    large_square_peg_adapter = SquarePegAdapter(peg=large_square_peg, radius=10)

    hole.fits(small_square_peg_adapter)  # True, the adapted square peg fits into the hole
    hole.fits(large_square_peg_adapter)  # False, the adapted square peg is too large for the hole
