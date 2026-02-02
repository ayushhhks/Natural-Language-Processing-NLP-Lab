##how would u use reg exp to identify all phone numbers in a text document, regardless of their format
import re

# Regex pattern to match phone numbers in various formats
pattern = r"""
    (?:\+?\d{1,3}[\s-]?)?        # Optional country code (+91, +1, etc.)
    (?:\(?\d{2,4}\)?[\s-]?)?     # Optional area code with or without parentheses
    \d{3,4}[\s-]?                # First block of digits
    \d{3,4}[\s-]?                # Second block of digits
    \d{3,4}                      # Last block of digits
"""

# Sample text document
text = """
Call me at 123-456-7890 or (123) 456 7890.
My office number is +91 98765 43210 and my US contact is +1-202-555-0173.
Another format: 9876543210.
"""

# Find all matches (using re.VERBOSE to allow comments in regex)
matches = re.findall(pattern, text, re.VERBOSE)

print("Extracted phone numbers:", matches)