#!/usr/bin/env python3

def add(a, b):
    sum1 = a + b
    return sum1

def difference(a, b):
    #diff = a - b
    return (a - b)

def divide(a, b):
    return a / b

def integerDivide(a, b):
    return a // b

def mod(a, b):
    return a % b

def isEven(num):
    d =num % 2
    if d == 0:
        print(num, "is even")
    else:
        print(num, "is odd")


c = add(3,4)
d = difference(3, 4)
r = divide(7, 2)
t = integerDivide(7, 2)
print(c)
print(d)
print(r)
print(t)
print(mod(7, 2))
isEven(8)