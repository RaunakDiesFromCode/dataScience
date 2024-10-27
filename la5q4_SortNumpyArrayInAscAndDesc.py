# Write a program to sort a NumPy array in ascending order and descending order

import numpy as np
arr = np.array([10, 2, 8, 4])
sorted_arr_asc = np.sort(arr) # ascending order
print("Ascending order", sorted_arr_asc)
sorted_arr_dsc = np.sort(arr)[::-1] # descending order
print("Descending order", sorted_arr_dsc)