# Write a program to check if a given string is a valid phone number. Assume valid phone numbers are of the form 123-456-7890.

import re
def is_valid_phone_number(phone_number):
# Regular expression pattern for the phone number format 123-456-7890
    pattern = r'^\d{3}-\d{3}-\d{4}$'
    # Check if the phone number matches the pattern
    if re.match(pattern, phone_number):
        return True
    else:
        return False
phone_number = input("Enter a phone number: ")
if is_valid_phone_number(phone_number):
    print(f"{phone_number} is a valid phone number.")
else:
    print(f"{phone_number} is not a valid phone number.")