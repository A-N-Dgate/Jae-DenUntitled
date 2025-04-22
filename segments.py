from suporting_functions import *

def Introduction():
    welcome = open("descriptions/Introduction/welcome.txt")
    text = combineText(welcome)
    print(text)
    next = input("press enter when you're done adjusting settings \n>")

def Chapter1(reader, player):
    display_text(reader, "ChapterI", None, False, True)
    string_parsing1(reader, player)