'''
App Name: Interactive Dictionary(console)
Authour : Felender
Version : 1.0
python Version: 3
'''
import json
from difflib import get_close_matches

#Read the json external file
data = json.load(open("data.json"))

#Return searched word
#Check if a word is a close match

def translate(word):
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input( f"Did you mean {get_close_matches(word, data.keys())[0]}. Enter Y if yes, of N if no: ").upper()
        if yn == "Y" :
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "N":
            return "Word don't exist. Please double check"
        else:
            return "We didn't understand your entry"
    else:
        return "Word don't exist. Please double check"

#Get input from the user
word = input("Enter word: ").lower()


output = (translate(word))

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
