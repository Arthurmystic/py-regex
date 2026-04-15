import re

num = "123-456-7890"
date = "15-08-1992"

pattern1 = r"\b(\d{3})[-.\s]?(\d{3})[-.\s]?(\d{4})\b"
pattern2 = r"(\d{2})-(\d{2})-(\d{4})"

formated_phone_str = r"(\1) \2-\3" 
formated_date_str = r"\3/\1/\2"

newVal = re.sub(pattern1,formated_phone_str,num)
newDate = re.sub(pattern2,formated_date_str,date)
print (newVal)
print (newDate)