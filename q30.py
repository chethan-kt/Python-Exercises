"""

Question:
Define a function which can print a dictionary where the keys are numbers between 1 and 3 (both included) and the values are square of keys.

Hints:

Use dict[key]=value pattern to put entry into a dictionary.
Use ** operator to get power of a number.

"""

def fun():
    dict = {}
    for i in range(1,4):
        dict[i] = i**2

    for i in dict:
        print dict[i]

fun()
