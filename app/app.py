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