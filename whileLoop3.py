#!/usr/bin/env python3
# Not only username needs to be 'student',
# you only have 3 trials to enter
counter = 1
totaltrials = 3
username = input("Enter username: ")
while username != 'student': #as long as ...
    print("Incorrect user name, try again...")
    print("You have", (totaltrials - counter), "more trials")
    username = input('Enter username: ')
    counter += 1

#action base on counter value
    if (totaltrials - counter) == 0:
        print("Sorry, apparently you have forgotten your username...")
        print("Program Exiting...")
        break
    
print('You are logged in now...')