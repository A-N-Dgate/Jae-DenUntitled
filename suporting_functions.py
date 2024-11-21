from Reader import *
import time
import sys

def display_text(reader, chapter_name, file_name, intro=False):
    #i was about to Reader reader = new Reader(); isnt that insane...
    if intro:
        reader.getReader().load_file("descriptions/chapterIntro/%s.txt"%(chapter_name))
    else:
        reader.getReader().load_file("descriptions/%sparsing/%s.txt"%(chapter_name, file_name))
    reader.getReader().read()
    #end

def string_parsing1(reader):
    #one just in case I need to make more / create a general one
    locked = False
    fridge = False
    comp = False
    while not (locked and fridge and comp):
        time.sleep(2)
        inp = input(">")

        #first the general ones
        if inp == "quit":
            sys.exit()

        #string parsing begins


        #a sneeky test
        if inp == "test":
            display_text(reader, "chapterI", "test")

        #input not recognised
        else:
            print("You can't do that yet")



