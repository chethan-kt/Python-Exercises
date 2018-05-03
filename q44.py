"""

Question:
Define a class named American which has a static method called printNationality.

Hints:

Use @staticmethod decorator to define class static method.

"""

class American:
    def __init__(self, name):
        self.name = name

    def printName(self):
        print self.name
        
    @staticmethod
    def printNationality():
        print "American"

a1 = American("Tom")
a1.printName()
a1.printNationality()
American.printNationality()
        
