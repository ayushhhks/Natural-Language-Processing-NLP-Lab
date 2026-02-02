#Lab 1 - WAP given a piece of text, we want to split the text at all spaces including bew line characters and carriage return and punctuation marks too

import re

# Input text
text = """This is a sample text with some punctuation marks! Also, newlines and carriage returns.Let's split it."""

# Regex to split on spaces, newlines, carriage returns, and punctuation
words = re.split(r'[\s\W]+', text)

# Remove empty strings (if any)
words = [w for w in words if w]

print(words)                               
