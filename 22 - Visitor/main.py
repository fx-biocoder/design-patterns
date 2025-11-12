"""
Visitor Pattern - Design Patterns (GoF)

Author: Facundo Martínez (fx-biocoder)
Repository: https://github.com/fx-biocoder/design-patterns

Description:
This file contains an implementation for the Visitor design pattern, one of the 23 design patterns described by the
Gang of Four (GoF). This pattern allows for separating algorithms from the objects on which they operate.
This code is based on the concepts and examples presented in the book "Dive Into Design Patterns" by Alexey Naumov.

Components:
- Shape: Abstract interface defining common operations.
- Dot: Concrete shape representing a single point with coordinates.
- Circle: Concrete shape representing a circle.
- Rectangle: Concrete shape representing a rectangle.
- CompoundShape: Composite shape that contains a collection of other shapes.
- Visitor: Abstract interface defining visit methods for each concrete shape type.
- XMLExportVisitor: Concrete visitor that exports shape information in XML format.
- Application: Client class.

License:
CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/deed.en)
"""
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def move(self, x: int, y: int):
        raise NotImplementedError

    @abstractmethod
    def draw(self):
        raise NotImplementedError

    @abstractmethod
    def accept(self, visitor):
        raise NotImplementedError


class Dot(Shape):
    def __init__(self, _id: int):
        self.id = _id
        self.x = 0
        self.y = 0

    def move(self, x: int, y: int):
        self.x = x
        self.y = y

    def draw(self) -> None:
        print(f"Drawing dot at ({self.x},{self.y})")

    def accept(self, visitor: 'Visitor') -> None:
        visitor.visit_dot(self)


class Circle(Shape):
    def __init__(self, _id: int, radius: int):
        self.id = _id
        self.x = 0
        self.y = 0
        self.radius = radius

    def move(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def draw(self) -> None:
        print(f"Draw Circle at ({self.x}, {self.y}) with radius {self.radius}")

    def accept(self, visitor: 'Visitor') -> None:
        visitor.visit_circle(self)


class Rectangle(Shape):
    def __init__(self, _id: int, width: int, height: int):
        self.id = _id
        self.x = 0
        self.y = 0
        self.width = width
        self.height = height

    def move(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def draw(self) -> None:
        print(f"Draw Rectangle at ({self.x}, {self.y}) with width {self.width} and height {self.height}")

    def accept(self, visitor: 'Visitor') -> None:
        visitor.visit_rectangle(self)


class CompoundShape(Shape):
    def __init__(self, _id: int):
        self.id = _id
        self.shapes = []

    def add(self, shape: Shape) -> None:
        self.shapes.append(shape)

    def remove(self, shape: Shape) -> None:
        self.shapes.remove(shape)

    def move(self, x: int, y: int) -> None:
        for shape in self.shapes:
            shape.move(x, y)

    def draw(self) -> None:
        print(f"Draw CompoundShape {self.id}:")
        for shape in self.shapes:
            shape.draw()

    def accept(self, visitor: 'Visitor') -> None:
        visitor.visit_compound_shape(self)


class Visitor(ABC):
    @abstractmethod
    def visit_dot(self, dot: Dot):
        raise NotImplementedError

    @abstractmethod
    def visit_circle(self, circle: Circle):
        raise NotImplementedError

    @abstractmethod
    def visit_rectangle(self, rectangle: Rectangle):
        raise NotImplementedError

    @abstractmethod
    def visit_compound_shape(self, compound_shape: CompoundShape):
        raise NotImplementedError


class XMLExportVisitor(Visitor):
    def visit_dot(self, dot: Dot) -> None:
        print(f"<Dot id='{dot.id}' x='{dot.x}' y='{dot.y}'/>")

    def visit_circle(self, circle: Circle) -> None:
        print(f"<Circle id='{circle.id}' x='{circle.x}' y='{circle.y}' radius='{circle.radius}'/>")

    def visit_rectangle(self, rectangle: Rectangle) -> None:
        print(f"<Rectangle id='{rectangle.id}' x='{rectangle.x}' y='{rectangle.y}' width='{rectangle.width}' height='{rectangle.height}'/>")

    def visit_compound_shape(self, compound_shape: CompoundShape) -> None:
        print(f"<CompoundShape id='{compound_shape.id}'>")
        for shape in compound_shape.shapes:
            shape.accept(self)
        print(f"</CompoundShape>")


class Application:
    def __init__(self):
        self.all_shapes = []

    def add_shape(self, shape: Shape) -> None:
        self.all_shapes.append(shape)

    def export(self) -> None:
        export_visitor = XMLExportVisitor()
        for shape in self.all_shapes:
            shape.accept(export_visitor)
