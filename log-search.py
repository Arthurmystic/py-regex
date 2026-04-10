result = []

def search(filename, text):
    with open(filename) as f:
      for x in f:
        searched_text = [line for line in f if text in line]
        result.append(searched_text)
        print (result)
        # for line in f:
        #     if text in line:
        #         # print(line)
        #         result.append(line)
        # print(result)

result2 = []

def joint_search(filename, text, text2):
    with open(filename) as f:
      searched_text = [line for line in f if text in line and text2 in line]
      result2.append(searched_text)
      print (result2)
        # for line in f:
        #     if text in line and text2 in line:
        #         print(line)
        #         result2.append(line)

joint_search('Secure.log', 'Failed', '3187')


# search('secure.log', 'nobody')
