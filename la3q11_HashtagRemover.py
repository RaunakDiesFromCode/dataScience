# Write a program that removes all hashtags from a given text

import re
text = "I love #Python and #coding. #HappyCoding"
# Regular expression pattern to match hashtags
hashtag_pattern = r'#\w+'
# Substitute hashtags with an empty string
cleaned_text = re.sub(hashtag_pattern, '', text)
# Remove any extra spaces left after removing hashtags
cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()
print(cleaned_text)