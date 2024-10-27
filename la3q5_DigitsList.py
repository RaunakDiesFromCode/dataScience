# Write a program for remove of all character from a string except integer and returns a list of all the digits in the string.

# Define a sample string
sample_string = "Hello, World! 123"
# Initialize an empty string to store the result
digits_only = ""
# Initialize an empty list to store the digits
digits_list = []
# Iterate through each character in the string
for char in sample_string:
    if char.isdigit():
        digits_only += char
        digits_list.append(char)
# Print the result
print(f"The string with only digits is: '{digits_only}'")
print(f"The list of digits in the string is: {digits_list}")