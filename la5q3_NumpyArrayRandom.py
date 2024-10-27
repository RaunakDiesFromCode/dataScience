# Write a program using numpy to create an array of size 6 where the elements of array are random numbers between 10 to 30

import numpy as np
# Create an array of size 6 with random integers between 10 and 30
random_array = np.random.randint(10, 31, size=6)
# Display the array

print("Random Array:", random_array)