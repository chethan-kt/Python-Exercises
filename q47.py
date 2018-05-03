"""

Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a method which can compute the area. 

Hints:

Use def methodName(self) to define a method.

"""

class Rectangle:
    def __init__(self,l,b):
        self.len = l
        self.bre = b

    def area(self):
        print "Area of a rectangle is ", self.len*self.bre


R1 = Rectangle(2,3)
R1.area()
