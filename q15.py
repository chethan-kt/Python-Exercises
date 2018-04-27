'''

Question 15
Level 2

Question:
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

'''

n = raw_input()
n1 = int(("%s" %n))
n2 = int(("%s%s" %(n,n)))
n3 = int(("%s%s%s" %(n, n,n)))
n4 = int(("%s%s%s%s" %(n,n,n,n)))
print n1+n2+n3+n4
