# write a program to do the following tasks
#   take a number and return its square root using math.sqrt()
#   take a number and return its factorial using math.factorial()
#   take 2 number and return the power of the first number raised to the second number using math.pow()
#   take 2 number and return the GCD of the two numbers using math.gcd()
#   take a floating point number and return the ceiling and floor value using math.ceil() and math.floor()

import math

number = 16
print(f"Square root of {number}:", math.sqrt(number))

number = 5
print(f"Factorial of {number}:", math.factorial(number))

num1 = 2
num2 = 3
print(f"{num1} raised to the power {num2}:", math.pow(num1, num2))

num1 = 12
num2 = 18
print(f"GCD of {num1} and {num2}:", math.gcd(num1, num2))

number = 3.14
print(f"Ceiling value of {number}:", math.ceil(number))
print(f"Floor value of {number}:", math.floor(number))

