# Write a program to extract dates from a text. The dates should be in the format dd-mm-yyyy or dd/mm/yyyy.

import re
# Define a sample text containing dates
sample_text = "Today's date is 12-08-2024. Tomorrow's date will be 13/08/2024. The project started on 01-01-2023 and ended on 31/12/2023."
# Define the regular expression pattern for dates in dd-mm-yyyy or dd/mm/yyyy format
date_pattern = r'\b\d{2}[-/]\d{2}[-/]\d{4}\b'
# Use the findall method to extract all matching dates
dates = re.findall(date_pattern, sample_text)
# Print the extracted dates
print("Extracted dates:", dates)