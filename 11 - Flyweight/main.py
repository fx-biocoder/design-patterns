"""
Flyweight Pattern - Design Patterns (GoF)

Author: Facundo Martínez (fx-biocoder)
Repository: https://github.com/fx-biocoder/design-patterns

Description:
This file contains an implementation for the Flyweight design pattern, one of the 23 design patterns described
by the Gang of Four (GoF). This pattern allows for keeping more objects in the available RAM by sharing the common
parts of the state between several objects, instead of keeping all the information inside each object.
This code is based on the concepts and examples presented in the book "Dive Into Design Patterns" by Alexey Naumov.

Components:
- TreeType: A flyweight object
- TreeFactory: Flyweight factory that manages a group of existent flyweight objects (i.e., tree types)
- Tree: Main class for trees
- Forest: Class for grouping trees

License:
CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/deed.en)
"""
from typing import Any


class TreeType:
    def __init__(self, name: str, color: str, texture: Any):
        self._name = name
        self._color = color
        self._texture = texture

    @property
    def name(self) -> str:
        return self._name

    @property
    def color(self) -> str:
        return self._color

    @property
    def texture(self) -> Any:
        return self._texture

    def draw(self, **kwargs) -> None:
        print(f"Drawing {self._name} at ({kwargs['x']},{kwargs['y']}) in {kwargs['canvas']}")


class Tree(TreeType):
    def __init__(self,
                 x: int,
                 y: int,
                 _type: TreeType,
                 **kwargs):
        super().__init__(kwargs['name'], kwargs['color'], kwargs['texture'])
        self.x = x
        self.y = y
        self.type = _type

    @staticmethod
    def draw(canvas: Any) -> None:
        print(f"Drawing tree at {canvas}")


class TreeFactory:
    def __init__(self):
        self._tree_types = {}

    def get_tree_type(self,
                      name: str,
                      color: str,
                      texture: Any) -> TreeType:
        key = (name, color, texture)
        if key not in self._tree_types:
            print(f"Creating new TreeType: {key}")
            self._tree_types[key] = TreeType(name, color, texture)
        else:
            print(f"Reusing existing TreeType: {key}")
        return self._tree_types[key]


class Forest:
    def __init__(self, tree_factory: TreeFactory):
        # Modified the constructor so that it includes the tree factory
        self.tree_factory = tree_factory
        self.trees = []

    def plant_tree(self,
                   x: int,
                   y: int,
                   name: str,
                   color: str,
                   texture) -> None:
        tree_type = self.tree_factory.get_tree_type(name, color, texture)
        tree = Tree(x, y, tree_type)
        self.trees.append(tree)

    def draw(self, canvas: Any) -> None:
        for tree in self.trees:
            tree.draw(canvas)
