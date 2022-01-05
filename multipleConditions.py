#!/usr/bin/env python3

# conditional statements with multiple pathways
# points greater than 90 ==> 'A'
# points greater than 80 ==> 'B'
# points greater than 70 ==> 'C'
# or else ==> 'F'

'''
Block comment
Python will ignore everything within this pair of 


'''
points = int(input("Enter points: "))
if points > 90:
    print("Congratulations!!! You got an 'A'")
elif points > 80:
    print("You got a 'B' ")
elif points > 70:
    print("Study harder next time, you got a 'C' ")
else:
    print("You failed. Your grade is 'F' ")

