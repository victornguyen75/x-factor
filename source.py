'''
Given any two numbers, this program can help the user
decide if the first number is divisible by the second
number. This program can validate for positive
integers.

Created by:    Victor Nguyen
Updated on:    12/12/2016
'''
while True:
    try:
        firstNum = int(input("Please enter the first positive integer: "))
        if firstNum < 0:
            raise ValueError
        secondNum = int(input("Please enter the second positive integer: "))
        if secondNum < 0:
            raise ValueError
        break
    except ValueError:
        print("Value error. Remember that this program"
              " will only take positive INTEGERS. Starting over.\n")
