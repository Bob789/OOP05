import math

from abc import ABC, abstractmethod
from typing import override

# abstract class
class Shape(ABC):
    def __init__(self, name: str):
        #self._name = name  # private --> access only from the class itself
        self._name = name  # protected --> access only from the class and its subclass

        # protected is not fully supported in python
        self._number_of_pixels = 0;  # protected --> access only from the class + subclasses

    @abstractmethod
    def calc_area(self):
        pass

    @abstractmethod
    def calc_hekef(self):
        pass

    def __my_presonal_stuff(self):
        pass

    @property
    def name(self):
        self.__my_presonal_stuff()
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) > 5:
            self.__name = value

    @override
    def __str__(self):
        return f"[Shape] name: {self.name} hekef: {self.calc_hekef(): .2f}" +\
               f"area: {self.calc_area(): .2f}"

s1 = Shape('rectangle') # abstract is not fully supported in python, unless you declare abs method
print(s1.name)

print(s1._number_of_pixels)  # possible, bad practice
s1.name = 'danny'

class Triangle(Shape):
    def __init__(self, name: str, a: float, b: float, c: float, h: float):
        # step 1
        super().__init__(name)
        # step 2
        self._a = a
        self._b = b
        self._c = c
        self._h = h

    @property
    def a(self):
        return self._a

    @property
    def b(self):
        return self._b

    @property
    def c(self):
        return self._c

    @property
    def h(self):
        return self._h

    @override
    def calc_hekef(self):
        # Perimeter
        return self.a + self.b + self.c

    @override
    def calc_area(self):

        # print (self.name)
        # print (super().name)  # bad practice

        # self._number_of_pixels += 1  # can access
        return self.c * self.h / 2

    @override
    def __str__(self):
        return f"{super().__str__()} [Triangle] a:{self.a} b:{self.b} " +\
            f"c: {self.c} h:{self.h}"

class TriangleEqualSides(Triangle):
    def __init__(self, name: str, a: float, c: float, h: float):
        super().__init__(name, a, a, c, h)

    @override
    def calc_hekef(self):
        # Perimeter
        return self.a * 2 + self.c

    @override
    def __str__(self):
        return f"{super().__str__()} [TriangleEqualSides]"

class TriangleAllSidesEqual(Triangle):
    def __init__(self, name: str, a: float, h: float):
        super().__init__(name, a, a, h)

    @override
    def calc_hekef(self):
        # Perimeter
        return self.a * 3

    @override
    def __str__(self):
        return f"{super().__str__()} [TriangleAllSidesEqual]"

class Rectangle(Shape):

    def __init__(self, name: str, a: float, b: float):
        super().__init__(name)
        self._a = a
        self._b = b

    @property
    def a(self):
        return self._a

    @property
    def b(self):
        return self._b

    @override
    def calc_hekef(self):
        # Perimeter
        return self.a * 2 + self.b * 2

    @override
    def calc_area(self):
        return self.a * self.b

    @override
    def __str__(self):
        return f"{super().__str__()} [Rectangle] a:{self.a} b:{self.b}"

class Square(Rectangle):

    def __init__(self, name: str, a: float):
        super().__init__(name, a, a)

    @override
    def calc_hekef(self):
        # Perimeter
        return self.a * 4

    @override
    def calc_area(self):
        return self.a ** 2

    @override
    def __str__(self):
        return f"{super().__str__()} [Sqaure]"

t = Triangle('tr1', 3.5, 4.4, 1.8, 4.0)
print(t)
print(t.calc_hekef())

'''
@property
@__.setter
@override
'''