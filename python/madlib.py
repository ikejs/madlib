from termcolor import colored, cprint
import nltk
# nltk.download('wordnet')
# ^ Remove hash on first run to download!
from nltk.corpus import wordnet as wn


userInput = [
    raw_input("Enter a plural noun: "),
    raw_input("Enter a place: "),
    raw_input("Enter a noun: "),
    raw_input("Enter a plural noun: "),
    raw_input("Enter a noun: "),
    raw_input("Enter an adjective: "),
    raw_input("Enter a verb: "),
    raw_input("Enter a number: "),
    raw_input("Enter an adjective: "),
    raw_input("Enter a body part: "),
    raw_input("Enter a verb: ")
]

wordTypes = [
    "n",
    "n",
    "n",
    "n",
    "n",
    "a",
    "v",
    "n",
    "a",
    "a",
    "v"
]

def getWordType(letter):
    if letter == "n":
        return "a noun"
    if letter == "v":
        return "a verb"
    if letter == "a":
        return "an adjective"

#CHECKING FOR WRONG INPUT
# https://stackoverflow.com/questions/35462747/how-to-check-a-word-if-it-is-adjective-or-verb-using-python-nltk
w = 0
while w <=10:
    if wn.synsets(userInput[w])[0].pos() !=  wordTypes[w]:
        print(colored(userInput[w], attrs=['bold']) + " is not " + getWordType(wordTypes[w]))
    w += 1

storyText = [
    "  Two "+colored(userInput[0], attrs=['bold'])+", both alike in dignity,",
    "  In fair "+colored(userInput[1], attrs=['bold'])+", where we lay our scene,",
    "  From ancient "+colored(userInput[2], attrs=['bold'])+" break to new mutiny,",
    "  Where civil blood makes civil hands unclean.",
    "  From forth the fatal loins of these two foes",
    "  A pair of star-cross`d "+colored(userInput[3], attrs=['bold'])+" take their life;",
    "  Whole misadventured piteous overthrows",
    "  Do with their "+colored(userInput[4], attrs=['bold'])+" bury their parents` strife.",
    "  The fearful passage of their "+colored(userInput[5], attrs=['bold'])+" love,",
    "  And the continuance of their parents` rage,",
    "  Which, but their children`s end, nought could "+colored(userInput[6], attrs=['bold'])+",",
    "  Is now the "+colored(userInput[7], attrs=['bold'])+" hours` traffic of our stage;",
    "  The which if you with "+colored(userInput[8], attrs=['bold'])+" "+colored(userInput[9], attrs=['bold'])+" attend,",
    "  What here shall "+colored(userInput[10], attrs=['bold'])+", our toil shall strive to mend.",
]

i = 0
print("*_______________________________________________________________________*")
while i < len(storyText):
    print(storyText[i])
    i += 1
print("*_______________________________________________________________________*")
print("Romeo and Juliet Prologue Source: https://www.madtakes.com/libs/186.html")
