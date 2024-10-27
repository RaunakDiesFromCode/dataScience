# write a program to take a list of numbers and return a new list with each number squared using the map() function and a lambda function.

import random

# Define a sample list
sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Square each element in the list
squared_list = list(map(lambda x: x**2, sample_list))
print("Squared list:", squared_list)
