"""

Question:
Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No". 

Hints:

Use if statement to judge condition.


"""

s = raw_input()

if s == 'YES' or s == 'yes' or s =='Yes':
    print "Yes"
else:
    print "No"
        
