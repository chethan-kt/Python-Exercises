"""

Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.

Hints:

To override a method in super class, we can define a method with the same name in the super class.


"""

class Shape:
    def __init__(self):
        pass
    def area(self):
        print "Area of a Share is 0" 

class Square(Shape):
    def __init__(self, len):
        Shape.__init__(self)
        self.len = len

    def area(self):
        print "Area of a square is ", self.len*self.len

s1 = Shape()
s1.area()
s2 = Square(2)
s2.area()
