#!/usr/bin/env python3

# simple if-else program

response = input("Enter state of service (running/stopped): ")

# select based on response
if response == "running":
    print("Service is running")
else:
    print("Service is not running")
