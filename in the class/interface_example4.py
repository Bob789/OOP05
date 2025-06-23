

from abc import ABC, abstractmethod
from typing import override

class INewCodeFormat(ABC):
    pass

class Shape(ABC):

    @abstractmethod
    def draw(self):
        pass

class Circle(Shape):

    def draw(self):
        print("Drawing a circle")

class Oval(Shape, INewCodeFormat):
    def draw(self):
        print("Drawing an oval")

class Square(Shape, INewCodeFormat):
    def draw(self):
        print("Drawing a square")

def draw_shape(s: Shape):
    s.draw()

def value_code(c):
    if isinstance(c, INewCodeFormat):
        print('best code!')