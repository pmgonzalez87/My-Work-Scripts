#!/usr/bin/env python3

import time

numbers = [1,2,3,4,5,6,7,8,9,10]
print(numbers)

#pull the "5th" item (index = 4)
print(numbers[4])

# create a computers list
computers = ["dc1", "dc2", "dhcp1", "web1", "web2"]
for c in range(2, 5): 
    print("rebooting", computers[c])

print()
# Skip dc1 and dc2
print("Skipping DC1 and DC2")
for p in computers: # p will have "dc1", dc2, dhcp1, web1...
    if p == "dc1" or p == "dc2":
        continue # don't do anything
    else:
        print("rebooting", p)

print()
numbers = [1,2,3,4,5,6,7,8,9,10]
# Slicing
print(numbers[3], numbers[5])
print(numbers[2:6]) # start from 2 and end with 6-1 index
print(computers[0:3]) # start with [0] and end with [3-1]

# Add to existing list
computers.append("db1")
print(computers)

computers.append("db2")
print(computers)

computers.insert(2,"ceopc")
print(computers)

computers.remove("dhcp1")
print(computers)

# simulating a dhcp server
counter = 0
computers = ["dc1", "dc2", "dhcp1", "web1", "web2"]
ipAddresses = ['1.1.1.1', '1.1.1.2', '1.1.1.3', '1.1.1.4']
for i in ipAddresses:
    print("assigning...", i, "to", computers[counter])
    counter += 1
    ipAddresses.remove(i)
    time.sleep(1)

print(ipAddresses)