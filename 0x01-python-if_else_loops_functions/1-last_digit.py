#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = int(repr(number)[-1])
if last_digit > 5 and number > 0:
        print("Last digit of", number, "is", last_digit, "and is greater than 5\n")
elif last_digit > 5 and number < 0:
        print("Last digit of", number, "is", -abs(last_digit), "and is less than 5\n")
elif last_digit == 0:
        print("Last digit of", number, "is", last_digit, "and is 0\n")
elif last_digit < 6 and not(0):
    if number < 0:
        print("Last digit of", number, "is", -abs(last_digit), "and is less than 6 and not 0\n")
    else:
        print("Last digit of", number, "is", last_digit, "and is less than 6 and not 0\n")
