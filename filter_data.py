# Using line.split() to search for a specific text in a line.

result = []

def search(filename, text, text2):
    with open(filename) as f:
        for line in f:
            if text in line and text2 in line:
                print(line)
                # modify the two lines below
                result.append(f"Day is {line.split()[0]} The user is  {line.split()[12]} and they tried to connect over {line.split()[16]}")
                print(result)
                
search('secure.log', 'Failed', '3187')
