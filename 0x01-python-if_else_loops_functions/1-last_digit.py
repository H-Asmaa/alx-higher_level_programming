#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = abs(number) % 10
if number < 0:
    last *= -1
if last == 0:
    str = "is 0"
elif last > 5:
    str = "is greater than 5"
elif last < 6:
    str = "is less than 6 and not 0"
print("Last digit of", number, "is", last, "and", str)
