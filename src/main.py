from pyblinkpico import *
from machine import ADC, Pin 
import time, random


# GLobals
# These are the pins you will use for making the hardware addition
aPin = Pin(15, Pin.OUT)
bPin = Pin(14, Pin.OUT)
cPin = Pin(13, Pin.OUT)
sumPin = Pin(12, Pin.IN)
carryoutPin = Pin(11, Pin.IN)


# Helpers

# Get a random integer
def generateRandomByte():
    return random.randint(0, 256)


# Row from 0-7 and number to be shown in binary format
def displayRow(row, number):
    pass # complete this code yourself


# bitSum takes two bits (b1 and b2) and add them
# the function returns a tuple with the result (0 or 1)
# and the carryover (0 or 1)
# the addition is done in hardware (write a/b/c pins and read sumPin/carryoutPin)
def bitSum(b1, b2, carry):
    result = 0
    carry = 0
    # PLACEHOLDER: put here your code
    # to compute result and carryover
    return (result, carry)


# sumRow takes two numbers (n1 and n2) which are 5 bits longs
# and sum them together. The results is a 8-bits long number
# the carryover (0 or 1) shows whether the addition overflowed
# sumRow calls bitSum because the addition is performed in hardware
def sumRow(n1, n2):
    result = 0b10101  # a placeholder value in binary to change
    carry = 1  # a placeholder value in binary to change
    # PLACEHOLDER: put here your code
    # to compute result and carryover
    return (result, carry)


# This function generates two random numbers and add them together
# the display shows the numbers, the sum and eventual carryover
def testAddition():
    num1 = generateRandomByte()
    num2 = generateRandomByte()
    (result, carry) = sumRow(num1, num2)
    displayRow(0, num1)
    displayRow(1, num2)
    displayRow(6, result)
    displayRow(7, carry)


# Main
# Wait before we start
display.fill(0)
display.blink_rate(Matrix.NO_BLINK)
display.auto_show(True)
time.sleep_ms(500)

# Compute
testAddition()

while True:
    if button_a.is_pressed() or button_b.is_pressed() or button_c.is_pressed():
        testAddition()
        time.sleep_ms(500)

