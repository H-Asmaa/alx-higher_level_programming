#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = abs(number) % 10
if last > 5 and number > 0:
    str = "is greater than 5 and not 0"
elif last > 5 and last > 0 and number < 0:
    str = "is less than 6 and not 0"
    last *= -1
elif last < 6 and last > 0:
    str = "is less than 6 and not 0"
elif last < 6 and last > 0 and number < 0:
    str = "is less than 6 and not 0"
    last *= -1
else:
    str = "is 0"
print("Last digit of", number, "is", last, "and", str)
