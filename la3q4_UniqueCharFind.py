# Write a program to count all letter, digit and special symbol from a given string

# Define a sample string
sample_string = "Hello, World! 123"
# Initialize counters

letter_count = 0
digit_count = 0
special_symbol_count = 0
# Iterate through each character in the string
for char in sample_string:
    if char.isalpha():
        letter_count += 1
    elif char.isdigit():
        digit_count += 1
    elif not char.isspace():
        special_symbol_count += 1
# Print the results
print(f"Total letters: {letter_count}")
print(f"Total digits: {digit_count}")
print(f"Total special symbols: {special_symbol_count}")