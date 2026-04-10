import re # Regular expressions module for pattern matching
import sys

test = input('Password? ')

# ITERATION METHOD:
def iteration_method(test):
    # Length check
    if 8 <= len(test) <=12:
        print('Passed length check')
    else:
        print('Failed length check')
        sys.exit()

    # Lowercase check
    for char in test:
        k = char.islower()
        if k == True:
            print('passed lowercase check')
            break
    if k != 1:
        print('failed lowercase check')
        sys.exit()

    # Digit check
    for char in test:
        d = char.isdigit()
        if d == True:
            print('passed digit check')
            break
    if d != 1:
        print('failed digit check')
        sys.exit()

    # Special character check
    special_chars = "!@#$%^&*"
    has_special = False
    for char in test:
        if char in special_chars:
            has_special = True
            print('passed special character check')
            break
    if not has_special:
        print('failed special character check')
        sys.exit()

    # Uppercase check
    for char in test:
        u = char.isupper()  
        if u == True:
            print('passed uppercase check \n' + test + ' Is a strong password')
            break
    if u != 1:
        print('failed uppercase check')
        sys.exit()

# ONESTEP VALIDATION WITH REGEX

def validate_password(test):
    # pattern
    pattern = r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*]).{8,}$"

    # Password Validation
    match = re.match(pattern, test)

    # True if the password matches the pattern
    validity = (bool(match))
    if validity == True:
        print('Password is valid')
    else:
        print('Password is invalid')


if __name__ == "__main__":
    print ("Which method do you want to use for password validation? \n1. Iteration method \n2. Regex method")
    choice = input("Enter your choice (1 or 2): ")

    while choice not in ["1", "2"]:
        print("Invalid choice. Please enter 1 or 2.")
        choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        print ("==========VALIDATION WITH ITERATION METHOD=============")
        iteration_method(test)
    elif choice == "2":
        print ("==========VALIDATION WITH REGEX=============")
        validate_password(test)
    else:
        print("Invalid choice. Please enter 1 or 2.")

    