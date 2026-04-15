import re
from typing import List
import argparse

# Step 2 - Text Search and Extraction

def find_all_digits(text: str) -> List[str]:
    """	Return all sequences of digits in the text."""
    return re.findall(r'\d+', text)
  

def find_all_words(text: str) -> List[str]:
    """Return a list of all words (alphanumeric + underscore) in the text."""
    return re.findall(r"\w+", text)


def find_all_whitespace(text: str) -> List[str]:
    """Return a list of all whitespace characters in the text."""
    return re.findall(r"\s",text)

def find_capitalized_words(text: str) -> List[str]:
    """Return words that start with a capital letter followed by lowercase letters."""
    return re.findall(r"\b[A-Z][a-z]+\b",text)


def find_five_digit_numbers(text: str) -> List[str]:
    """Return all digit sequences that are exactly 5 digits long."""
    return re.findall(r"\b\d{5}\b",text)


def find_words_starting_with_capital(text: str) -> List[str]:
    """Return all words that begin with a capital letter, regardless of what's after."""
    return re.findall(r"\b[A-Z][\w!@#$%^&*()+=-]+",text)

def match_lines_starting_with(text: str, prefix: str) -> List[str]:
    """Return lines from the text that start with a given prefix."""
    
    # 1. Break the large block of text into a list of individual strings.
    split_lines = text.splitlines()
    
    # 2. Prepare the regex pattern:
    # - 'fr': An f-string (to use the prefix variable) and a raw string (for regex safety).
    # - '^': The anchor that forces the match to start at the absolute beginning of the line.
    # - 're.escape()': Automatically adds backslashes to any special characters in the 
    #   prefix (like '.' or '*') so they are treated as literal text, not regex commands.
    pattern = fr"^{re.escape(prefix)}" 
    
    # 3. Optional: Compile the pattern for better performance if processing many lines.
    compiled_pattern = re.compile(pattern)
    
    # 4. Use a list comprehension to filter the lines:
    # - 're.match' or 'compiled_pattern.match' checks specifically starting at index 0.
    # - This ensures we only keep lines where the prefix was found at the start.
    desired_lines = [line for line in split_lines if re.match(pattern, line)]
    
    return desired_lines


def match_lines_ending_with(text: str, suffix: str) -> List[str]:
    """Return lines from the text that end with a given suffix."""
    split_lines = text.splitlines()
    pattern = fr"{re.escape(suffix)}$" 
    desired_lines = [line for line in split_lines if re.search(pattern,line)]
    return desired_lines

# Step 3 - Text Manipulation

def replace_vowels_with_astrisks(text: str) -> str:
    """Returns a string where all vowels from the input string have been replaced with an asterisks."""
    pattern = r"[aeiouAEIOU]"
    return re.sub(pattern,'*',text) # re.subn is same as re.sub while including count

def doubler_fn(m):
  num = int(m.group()) #m.group() strps out the value from the object m which re.sub() proveds in its secod argument
  return str (num*2)

doubler = lambda m: str(int(m.group())*2) # similar to doubler_fn above. just like an arrow fn in js ie doubler = (m)=>m*2
# 
def double_every_digit(text: str) -> str:
    """Return a new string where all integers have been doubled."""
    return re.sub(r"\d",doubler_fn,text) # also double_fn can work
# The 2nd arg of re.sub() can be a string or a callback function.
# If it's a function, re.sub() finds a match (ie, what is to be replaced),
# wraps it in a Match Object,and passes it into the function automatically
# (we only pass the function name). The callback function unwraps the 
# match by using .group()

def split_on_digits(text: str) -> List[str]:
    """Return an array of strings that where each string comes from the original and has been split on digits."""
    pattern = r"\d+"
    return re.split(pattern, text)

def split_on_a_specific_symbol(text: str) -> List[str]:
    """Return an array of strings that are the original string split on any symbol that matches '-', ':', or '|'."""
    pattern = r"[-:|]+"
    return re.split(pattern, text)

def split_on_capital_letters(text: str) -> List[str]:
    """Return a list of strings split before each capital letter."""
    pattern = r"(?=[A-Z])"
    return re.split(pattern, text)

# Step 4 - Real Life Examples

def extract_dates(text: str) -> List[str]:
    """
    Extract and return a dictionary with 'month', 'day', and 'year' keys if a date is found.
    """
    # We wrap the parts we want to 'keep' in parentheses. 
    # findall() will see these 3 groups and pack them into a tuple automatically.
    date_pattern = r"(\d{2})[-\/](\d{2})[-\/](\d{4})" # curved brackets are only exclusionary with findall. for other functions like search etc, they are not
  # pattern = r'\b(0[1-9]|1[0-2])[-/](0[1-9]|[12][0-9]|3[01])[-/](\d{4})\b'
    dates = re.findall(date_pattern, text)
    return dates

def is_valid_email(email: str) -> bool:
    """
    Return True if the input is a valid email address, otherwise False.
    """
    pattern = r"[\w.-]+\@\w+\.\w+(\.\w+)?" #\w includes all alphanumeric and _ too
    return bool(re.fullmatch(pattern, email))

def extract_named_date(text: str) -> dict[str, str] | None:
    """
    Extracts a date and returns a dictionary with 'month', 'day', and 'year' keys. 
    Return a dictionary that contains month, day, and year with the appropiate values.
    """
    pattern = r"\b(?P<month>0[1-9]|1[012])[-\/](?P<day>0[1-9]|[12][0-9]|3[01])[-\/](?P<year>\d{4})\b"
    match = re.search(pattern,text)
    return match.groupdict() if match else None

def normalize_phone_number(text: str) -> str:
    """
    Normalize phone numbers in the text to the format (XXX) XXX-XXXX.
    Return a new string that replaces provided numbers with the normalized format.
    """
    pattern = r"\b(\d{3})[\-\.\s]?(\d{3})[\-\.\s]?(\d{4})\b"
    replacement_string = r"(\1) \2-\3"
    return re.sub(pattern, replacement_string,text)

def is_valid_zip(zipcode: str) -> bool:
    """
    Return True if the input is a valid US ZIP code (5-digit or ZIP+4 format), otherwise False.
    """
    pattern = r"\d{5}(-\d{4})?"
    return bool(re.fullmatch(pattern,zipcode))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run regex functions.")
    parser.add_argument("step", choices=["step2", "step3", "step4"], help="Which step to run")
    parser.add_argument("task", help="Which task to run")
    parser.add_argument("text", help="Text to process")
    parser.add_argument("prefixOrSuffix", nargs="?", help="Prefix or suffix (only needed for some tasks)")

    args = parser.parse_args()

    # Step 2 mappings
    step2_tasks = {
        "task1": find_all_digits,
        "task2": find_all_words,
        "task3": find_all_whitespace,
        "task4": find_capitalized_words,
        "task5": find_five_digit_numbers,
        "task6": find_words_starting_with_capital,
        "task7": match_lines_starting_with,  # Needs prefixOrSuffix
        "task8": match_lines_ending_with     # Needs prefixOrSuffix
    }

    # Step 3 mappings
    step3_tasks = {
        "task1": replace_vowels_with_astrisks,
        "task2": double_every_digit,
        "task3": split_on_digits,
        "task4": split_on_a_specific_symbol,
        "task5": split_on_capital_letters
    }

    # Step 4 mappings
    step4_tasks = {
        "task1": extract_dates,
        "task2": is_valid_email,
        "task3": extract_named_date,
        "task4": normalize_phone_number,
        "task5": is_valid_zip
    }

    # Which step to use
    steps = {
        "step2": step2_tasks,
        "step3": step3_tasks,
        "step4": step4_tasks
    }

    selected_tasks = steps.get(args.step)

    if selected_tasks is None:
        print(f"Invalid step: {args.step}")
    else:
        func = selected_tasks.get(args.task)

        if func is None:
            print(f"Invalid task {args.task} for {args.step}")
        else:
            if args.step == "step2" and args.task in ("task7", "task8"):
                # Special case: match_lines_starting_with or match_lines_ending_with need two arguments
                if args.prefixOrSuffix is None:
                    print(f"Error: 'prefixOrSuffix' argument is required for {args.task}.")
                else:
                    print(func(args.text, args.prefixOrSuffix))
            else:
                print(func(args.text))
