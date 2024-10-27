# Write a program using numpy package to find the lcm and hcf of two numbers

import numpy as np
# Input two numbers
num1 = 12
num2 = 18
# Find HCF (GCD)
hcf = np.gcd(num1, num2)
# Find LCM
lcm = abs(num1 * num1) // hcf
# Display the results
print("Number 1:", num1)
print("Number 2:", num2)
print("HCF (GCD):", hcf)
print("LCM:", lcm)