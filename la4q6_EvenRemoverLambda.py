# write a program to filter out all the evn numbers from a list using the filter() function and a lambda function.

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = list(filter(lambda x: x % 2 == 0, list1))
print("Even numbers:", even_numbers)