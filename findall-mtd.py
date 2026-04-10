# Uses findall() to find all matches of a pattern in a text. It returns a list of all matches found. If no matches are found, it returns an empty list.

import re

# Getting the contents of the file
textfile = open('final_search.log', 'r')
filetext = textfile.read()
textfile.close()

# Getting IP Addresses
# IP_Address = re.findall(r'(\d+\.){3}\d+', filetext)
IP_Address = re.findall(r'\d+\.\d+\.\d+\.\d+', filetext)
print(IP_Address)

# Getting Email Addresses

Email_Address = re.findall(r'\w+\@\w+\.\w+', filetext)
print(Email_Address)

# Getting Phone Numbers

Phone_Numbers = re.findall(r'\d+\-\d+\-\d+', filetext)
print(Phone_Numbers)
