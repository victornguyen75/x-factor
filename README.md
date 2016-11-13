# X Factor
###### A divisibility checker
It is a mathematical algorithm that verifies if a number is divisible by another number. Due to the rise of technology and computers, we can simply use the modulous operator to quickly satisfy this problem. However, in a situation that we do NOT have access to a calculator, the X Factor algorithm can be quite useful. Despite it's elaborate tediousness as a recursive algorithm, it can apply to any pair of numbers.

*Future versions of this program will avoid using the modulus operator (%)*

Psuedocode:
1. USER INPUT
  * Ask for a number to divide
  * Ask for a number that can be a factor of the first number
2 VALIDATION-FUNCTION: Check for only positive values	negative values will cause a while loop to ask for a positive value
3 VERIFICATION-FUNCTION: Ask the user if the number is "correct" (string = "correct")
  * 'Y', 'y', 'Yes', or 'yes' will continue the program
  * ''N', 'n', 'No', or 'no' will loop the program to the beginning
  * else will end the program
4 Multiply the input by a suitable number so that the product as a 9 in the ones place
*		while (True):
*			i = 1
*			xFactor = input * i		# Multiply by a suitable number
*			if ( xFactor % 10== 9 ): 
*				continue with the program
*				break
*			else:		
*				i+=1
5 Divide the xFactor by 10 and add 1 to get the true xFactor
*		xFactor = (xFactor / 10) + 1
6 Print the xFactor to the user
7 Modulus the first user inputted number by 10 to get the one's digit 
*		onesDigit = num % 10
8 Multiple that onesDigit by the xFactor to get the adjuster number
*		onesDigit *= xFactor
9 Divide the first user inputted number by 10, while truncating the following decimal values, to get the penultimate digits
*		penUlt = int(num / 10)
10 Add the new onesDigit number to the penultimate digits
*		penUlt += onesDigit
11 VERIFICATION-FUNCTION: Ask the user if the number is "divisible" (string = "divisible")
12  Recursively loop to step 4 if the answer is 'N', 'n', 'No', or 'no'
13 If 'Y', 'y', 'Yes', or 'yes', validate that with
*		if (num % input == 0):
*			print (num "is divisible by" input)
*		else:
*			print (num "is NOT divisible by" input)
14 End the program with "Thanks for using the program!" 
