# Write a program that finds the indices of elements in a NumPy array that satisfy multiple conditions(e.g., elements greater than 2 and less than 5)

import numpy as np
arr = np.array([1, 7, 3, 4])
indices = np.where((arr > 2) & (arr < 5))
print('Indices are', indices)
