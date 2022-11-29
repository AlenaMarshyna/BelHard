#  Написать класс Rectangle
# Конструктор класса принимает координаты точек по диагонали (правая нижняя, верхняя левая или левая нижняя, правая верхняя)
# Написать метод perimeter возвращающий периметр получившегося прямоугольника
# Написать метод square возвращающий площадь получившегося прямоугольникаы
# *учесть, что координаты на плоскости могут быть отрицательными

from math import *

class Rectangle:
    
    def __init__(self, x1: float, y1: float, x2: float, y2: float) -> None:
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    
    def perimeter(self) -> float:
        perimetr = abs(self.x1 - self.x2) * 2 + abs(self.y1 - self.y2) * 2
        return perimetr
    
    def square(self) -> float:
        sq = abs((self.x1 - self.x2) * (self.y1 - self.y2))
        return sq

rectangle1 = Rectangle(3.0, 2.0, -3.0, -2.0)
print(rectangle1.perimeter())
print(rectangle1.square())
