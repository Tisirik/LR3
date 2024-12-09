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