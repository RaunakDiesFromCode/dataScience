# Write a program that replaces all vowels in a string with a specific character (e.g., '*').

# Define a sample string
sample_string = "Hello, World!"
# Define the specific character to replace vowels
replacement_char = '*'
# Define the vowels
vowels = "AEIOUaeiou"
# Replace vowels in the string
modified_string = ''.join([replacement_char if char in vowels else char for char in
sample_string])
# Print the result
print(f"The modified string is: '{modified_string}'")