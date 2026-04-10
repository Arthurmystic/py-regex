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

search('secure.log', 'nobody')
