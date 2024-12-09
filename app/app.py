import math

class Shape:

    def __init__(self):
        self._shape_type = "Geometric Shape" 
    @staticmethod
    def about():
        print("Программа расчета объема геометрических фигур.")
        print("Разработано командой из трех человек, а именно Сираев Т.В. Хасянова И.И. Фатихов Р.С.")
    def calculate_volume(self):
        raise NotImplementedError("Этот метод должен быть переопределен в дочернем классе.")
class Sphere(Shape):

    def init(self, radius):
        super().init()  
        self._radius = radius  
        self._shape_type = "Sphere"  

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Радиус должен быть положительным числом.")
        self._radius = value

    def calculate_volume(self):
        return (4 / 3) * math.pi * self._radius**3
