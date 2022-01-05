#!/usr/bin/env python3

username = input("Enter username: ")
while username != 'student':
    print("Incorrect user name, try again...")
    username = input('Enter username: ')

print('You are logged in now...')