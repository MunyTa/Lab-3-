class Figure(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
    def info(self):
        return f"Площадь: {self.area():.2f}, Периметр: {self.perimeter():.2f}"
class Rectangle(Figure):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)
    def __str__(self):
        return f"Прямоугольник {self.width}x{self.height}"
class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2
    def perimeter(self):
        return 2 * math.pi * self.radius
    def __str__(self):
        return f"Круг радиусом {self.radius}"
class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
    def area(self):
        p = self.perimeter() / 2
        return math.sqrt(p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c))
    def perimeter(self):
        return self.side_a + self.side_b + self.side_c
    def __str__(self):
        return f"Треугольник со сторонами {self.side_a}, {self.side_b}, {self.side_c}"
if __name__ == "__main__":
    figures = [
        Rectangle(5, 3),
        Circle(4),
        Triangle(3, 4, 5)
    ]
    for figure in figures:
        print(f"{figure}: {figure.info()}")