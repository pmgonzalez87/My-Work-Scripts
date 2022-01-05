#!/usr/bin/env python3
import time

# Loop thru certain number if times
'''
for counter in range(10): # counter: 0,1,2,3,4,... 9 
    print(counter)

print()
print("This line prints outside of the loop above")

for counter in range(1, 10): # counter: 1,2,3...9
    print(counter, "Mississippi")
    time.sleep(1)

print("You counted 9 seconds")
'''
colors = ["red", "blue", "green", "yellow"]

for c in colors: # variable c: "red", "blue", green, yellow sequentially per loop
    print(c)
    # back up C Drive
    # back up D Drive
    # back up running config
    time.sleep(0.5)

print("End of Program...")
