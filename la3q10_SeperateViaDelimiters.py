# Write a program that splits a string by multiple delimiters (e.g., commas, semicolons, and spaces).

import re
input_string = "apple, orange;banana grape;pear"
# Define a regex pattern for the delimiters (commas, semicolons, and spaces)
pattern = r'[,\s;]+'
# Use re.split to split the string by the specified delimiters
split_result = re.split(pattern, input_string)
print("Split result:", split_result)