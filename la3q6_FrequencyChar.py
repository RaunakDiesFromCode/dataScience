# Write a program that counts the frequency of each character in a string and returns a dictionary with the characters as keys and their counts as values.

text = "hello world"
# Initialize an empty dictionary to store the frequency of each character
frequency_dict = {}

# Iterate through each character in the string
for char in text:
# If the character is already in the dictionary, increment its count
    if char in frequency_dict:
        frequency_dict[char] += 1
    # If the character is not in the dictionary, add it with a count of 1
    else:
        frequency_dict[char] = 1
print(frequency_dict)
