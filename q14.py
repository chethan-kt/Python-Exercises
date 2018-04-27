'''

Question 14
Level 2

Question:
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

'''

s = raw_input()
d = {'Upper':0,'Lower':0}
for i in s:
    if i.isupper():
        d['Upper'] += 1
    elif i.islower():
        d['Lower'] += 1
    else:
        pass

print 'Total number of Upper case letters:',d['Upper']
print 'Total number of Lower case letters:',d['Lower']
