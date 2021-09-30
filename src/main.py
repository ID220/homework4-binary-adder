from microbit import *
import random

# GLOBALS
BRIGHTNESS = 9
BIT_LENGTH = 5


def displayRow(row, number):
    if (number < 0 or number > 32):
        return

    for i in range(0, BIT_LENGTH):
        bit = (number >> i) & 1
        x = BIT_LENGTH-1-i
        display.set_pixel(x, row, bit*BRIGHTNESS)


def generateRandomNumber():
    return random.randint(0, 32)


# bitSum takes two bits (b1 and b2) and add them
# the function returns a tuple with the result (0 or 1)
# and the carryover (0 or 1)
def bitSum(b1, b2, carry):
    result = 0
    carry = 0
    # PLACEHOLDER: put here your code
    # to compute result and carryover
    return (result, carry)


# sumRow takes two numbers (n1 and n2) which are 5 bits longs
# and sum them together. The results is a 5-bits long number
# the carryover (0 or 1) shows whether the addition overflowed
def sumRow(n1, n2):
    result = 0b10101  # a placeholder value in binary
    carry = 1  # a placeholder value in binary

    # PLACEHOLDER: put here your code
    # to compute result and carryover
    return (result, carry)


# This function generates two random numbers and add them together
# the display shows the numbers, the sum and eventual carryover
def testAddition():
    num1 = generateRandomNumber()
    num2 = generateRandomNumber()
    (result, carry) = sumRow(num1, num2)
    displayRow(0, num1)
    displayRow(1, num2)
    displayRow(3, result)
    displayRow(4, carry)


# Main
testAddition()

while True:
    if button_a.is_pressed() or button_b.is_pressed():
        testAddition()
        sleep(500)
