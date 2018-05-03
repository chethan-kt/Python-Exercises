"""

Question:
Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area. 

Hints:

Use def methodName(self) to define a method.

"""

class Circle:
    def __init__(self, rad):
        self.radius = rad

    def area(self):
        print "Area of a circle is ", 3.14*(self.radius**2)


c1 = Circle(2)
c1.area()
