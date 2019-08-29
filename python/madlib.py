from termcolor import colored, cprint

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
