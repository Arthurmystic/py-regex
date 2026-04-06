# INTRO TO REGEX
r"""
Common Matching Patterns
\d : This character matches any digit [0-9]
\w : Matches any word character [a-z or A-Z]
\s : Any white space character
Common Quantitative Patterns
'+' : Matches one or more of a pattern. E.g \d+ means one or more digits
'?' : Means zero or one of a pattern
'*' : Means zero or more of a pattern
"""

# Escape Characters: \ used to escape special characters and treat 
# them as literal characters eg \. will match a literal dot instead of
#  any character or \@ will match a literal @ instead of being used in 
# email patterns

import re

# Email Addresses
def read_email(file):
    with open(file, 'r') as data:
        contents = data.read()
        result = re.search(r'\w+\@\w+\.\w+', contents) # re.search() returns the 1st match object found. To find all matches, we can use re.findall() instead.
        print(f"Read email: {result.group()}") # .group() extracts the matched string from the match object. If there are no matches, it will raise an AttributeError since result will be None. To avoid this, we can check if result is not None before calling .group().

# IP Addresses
def read_IP_Address(file):
    with open(file, 'r') as data:
        contents = data.read()
        result = re.search(r'(\d+\.){3}\d+', contents)
        print(f"Read IP address: {result.group()}")

# Address Finder
def Address_finder(file):
    with open(file, 'r') as data:
        contents = data.read()
        result = re.search(r'\d+\s\w+\s\w+\s\w+\s\#\d+\s\w+\s\w+\,\s\w+\s\d+\s\w+', contents)
        print(f"Read address: {result.group()}")

if __name__ == "__main__":
    file = 'info.txt'
    read_email(file)
    read_IP_Address(file)
    Address_finder(file)