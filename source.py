'''
Given any two numbers, this program can help the user
decide if the first number is divisible by the second
number. This program can validate for positive
integers.

SUBSTITUTION FOR MODULUS OPERATOR (%)
A-B * (A/B), where A and B are positive integers

Created by:    Victor Nguyen
Updated on:    12/12/2016
'''
# Function prototyping
# Character validation
def validate(char):
	while char != 'Y' and char != 'y' and char != 'N' and char != 'n':
            char = input("Invalid input. Please try again. Are those numbers correct? (Y/N) ")

# Defines variables
firstNum = 0
secondNum = 0
choice = 'y'
xFactor = 1
onesDigit = 0
penUlt = 0;

# INPUT VALIDATION
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

# INPUT VERIFICATION
print("Your first number is " + str(firstNum) + "\n and your second number is " + str(secondNum))
choice = input("Are these correct?")
validate(choice)

########################
# THE ALGORITHM BEGINS #
# This procedure       #
# creates the xFactor  #
########################

# Find a multiple of the second number 
# that has a 9 in the one's place
while xFactor - 10 * (xFactor/10) != 9:
    xFactor = secondNum * i
    i+=1

# Now, using the value in the ten's
# place, add 1
xFactor = (xFactor / 10) + 1
   
# Display to the user what
# the xFactor is
print("Your X Factor is " str(xFactor))

# Get the one's digit of the first number
onesDigit = firstNum - 10 * (firstNum/10)

# onesDigit is now the adjuster number
onesDigit *=xFactor

# Divide the first user inputted number by 10, while truncating the following decimal values, to get the penultimate digits
penUlt = int(firstNum/10)

# Add the new onesDigit number to the penultimate digits
penUlt += onesDigit

# Display a smaller number to check if this number
# is divisible by the second number inputted by the
# user
print("Is " + str(penUlt) + " divisible by " + str(secondNum) + "? ")

    
