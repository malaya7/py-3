import json, difflib

data = json.load(open("data.json"))

def translate(word):
    word = (word.lower())
    if word in data:        # ther word exits in json file
      return data[word]
    elif word.title() in data: # check for citis and names. title() return first char upper and lower the rest.
         return data[word.title()]
    elif word.upper() in data: #in case user enters words like USA or NATO
        return data[word.upper()]
    elif word[0].isupper() not in data: # Check for names.
        return "You Entered a name!"
    elif len(difflib.get_close_matches(word, data.keys())) > 0: # check for a similar word. get_close_matches return list
      response = input("Did you mean %s insetad? Enter Y(Yes) or N(no)" % difflib.get_close_matches(word, data.keys())[0])
      if response == "Y" or response == 'y':
          return data[difflib.get_close_matches(word, data.keys())[0]]
      else:
          return "That was the best match for your input!"
    else:
        return " The word not in the file!" # lastly the word not in the json file
word = input("Enter word: ")

result = translate(word) #sometimes the word have multiple def in a list
if type(result) == list:
    for i in result:
        print(i)
else:
    print(result)
