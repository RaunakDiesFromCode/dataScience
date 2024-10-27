# write a program that takes alist to do the following tasks
#   shuffle the list using random.shuffle()
#   return a random element from the list using random.choice()

import random

# Define a sample list
sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Shuffle the list
random.shuffle(sample_list)
print("Shuffled list:", sample_list)

# Return a random element from the list
random_element = random.choice(sample_list)
print("Random element from the list:", random_element)
