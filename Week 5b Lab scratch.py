#!/usr/bin/env python3

testPassword = input("Enter your Password: ")
UPPERCASE = 'ABCDEFGHIJKLMONPQRSTUVWXYZ'
upperCaseTest = False
lowercase = 'abcdefghijklmopqrstuvwxyz'
lowerCaseTest = False
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
numbersTest = False
specialSymbols = ['!', '@', '#', '$', '%', '^', '*', '(', ')', '_', '<', '>', '?']
specialSymbolsTest = False


#cycle thru each character of testPassword
for t in testPassword:
    #if you find the current char in UPPERCASE, then test pass
    if t in UPPERCASE:
        upperCaseTest = True
        break

if upperCaseTest == True:
    print('Your Password PASSED the Uppercase Test')
else:
    print('Your Password FAILED the Uppercase Test')


#cycle thru each character of testPassword
for l in testPassword:
    #if you find the current char in lowercase, then test pass
    if l in lowercase:
        lowerCaseTest = True
        break

if lowerCaseTest == True:
    print('Your Password PASSED the lowercase Test')
else:
    print('Your Password FAILED the lowercase Test')


#cycle thru each character of testPassword
for n in testPassword:
    #if you find the current char in numbers, then test pass
    if n in numbers:
        numbersTest = True
        break

if numbersTest == True:
    print('Your Password PASSED the numbers Test')
else:
    print('Your Password FAILED the numbers Test')


#cycle thru each character of testPassword
for s in testPassword:
    #if you find the current char in numbers, then test pass
    if s in specialSymbols:
        specialSymbolsTest = True
        break

if specialSymbolsTest == True:
    print('Your Password PASSED the special symbols Test')
else:
    print('Your Password FAILED the special symbols Test')

# checking for the minimum password length
if len(testPassword) < 8:
    print('Your Password PASSED the password length Test')
else:
    print('Your Password FAILED the password length Test')