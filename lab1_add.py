##Additional Questions
# Write a Regex Pattern to extract all dd mm yyyy dates from a gicven paragraph
import re

# Regex pattern for dd mm yyyy format
pattern = r"\b(0[1-9]|[12][0-9]|3[01])\s(0[1-9]|1[0-2])\s(19|20)\d{2}\b"

# Sample paragraph
text = """
I was born on 12 01 1995 and my sister was born on 05 07 2000.
We went on a trip on 31 12 2021, but not on 32 01 2020.
"""

# Find all matches
dates = re.findall(pattern, text)

# re.findall returns tuples because of groups, so join them back
formatted_dates = [" ".join(date) for date in dates]

print("Extracted dates:", formatted_dates)