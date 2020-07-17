class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.diameter = radius + radius
        self.area = (radius * radius) * 3.14
    def setRadius(self, radius):
        return self.radius
    def area(self, radius):
        return self.area
    def diameter(self, radius):
        return self.diameter
    def circumference(self, diameter):
        self.circumference = (3.14 * diameter)
        return self.circumference
    def __str__ (self):
        self.s1 = str(self.circumference)
        return self.s1

        
circle = Circle(5)
