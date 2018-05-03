"""

Write a function to compute 5/0 and use try/except to catch the exceptions.

Hints:

Use try/except to catch exceptions.

"""

def compute():
    try:
        print 5/0
    except ZeroDivisionError:
        print "division by zero error"
    except Exception, err:
        print "Exception caught"
    finally:
        print 'In finally block for cleanup'

compute()
