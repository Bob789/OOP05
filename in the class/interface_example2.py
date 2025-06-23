

from abc import ABC, abstractmethod
from typing import override


class IDrawRounded(ABC):
    @abstractmethod
    def draw_rounded(self):
        pass

class Shape(ABC):

    @abstractmethod
    def draw(self):
        pass

class Circle(Shape, IDrawRounded):
    def draw(self):
        print("Drawing a circle")

    @override
    def draw_rounded(self):
        print("Drawing a circle with rounded edges")

class Oval(Shape, IDrawRounded):
    def draw(self):
        print("Drawing an oval")

    @override
    def draw_rounded(self):
        print("Drawing an oval with smooth curves")

class Square(Shape):
    def draw(self):
        print("Drawing a square")

def draw_shape(s: Shape):
    s.draw()