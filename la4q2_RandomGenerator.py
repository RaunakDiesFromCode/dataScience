# write a program to return a random integer between a and b using random.randint() and random floating point number between 0 and 1 using random.random()

import random

a = 10
b = 20
random_int = random.randint(a, b)
print(f"Random integer between {a} and {b}:", random_int)

random_float = random.random()
print(f"Random floating point number between 0 and 1:", random_float)