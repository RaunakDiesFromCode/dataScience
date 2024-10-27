# Write a program that finds the index of a specific element in a NumPy array, index of the maximum element in a NumPy array and index of the minimum element in a NumPy array.

import numpy as np
arr = np.array([10, 2, 8, 4])
index = np.where(arr == 8)
max_index = np.argmax(arr)
min_index = np.argmin(arr)
print("Index of 8", index)
print('Index of max element', max_index)
print('Index of min element', min_index)
