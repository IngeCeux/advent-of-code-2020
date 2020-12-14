import numpy as np
import re
from fractions import gcd

input_file = open("input/day13.txt")
lines = str(input_file.read())
lines = lines.split('\n')

earliest = int(lines[0])
buses = lines[1].split(',')

buses = [bus for bus in buses if bus != 'x']

for i in range(len(buses)):
    if buses[i].isnumeric():
        buses[i] = int(buses[i])


bus_times = []

for bus in buses:
    time = bus
    while time < earliest:
        time += bus
    bus_times.append((bus, time))

closest = bus_times[0]
closest_diff = closest[1]-earliest

for time in bus_times:
    diff = time[1] - earliest
    if diff < closest_diff:
        closest = time
        closest_diff = diff

result = closest[0] * closest_diff

print(result)

# part 2


def lcm(a, b):
    return a*b // gcd(a, b)


buses = lines[1].split(',')

t = int(buses[0])  # Defining the start time equal to the first value in the
step = int(buses[0])  # This is what we will increment the time by
for x in buses[1:]:
    if x.isnumeric():  # Proceed only if x is a number
        while(True):
            # The index value of the number is how far it is from the first number
            if (t+buses.index(x)) % int(x) == 0:
                # print(t)
                break
            # incrementing time with LCM of current number in the loop and the previous number
            t += step
        # int(x)              #Making sure to take the LCM in case some number in the input is not a prime number
        step = lcm(step, int(x))
        print(step)

print('Part 2: ', t)
