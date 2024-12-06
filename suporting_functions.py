from Reader import *
import time
import sys

def display_text(reader, chapter_name, file_name, para=False, intro=False):
    #i was about to Reader reader = new Reader(); isnt that insane...
    if intro and not para:
        reader.getReader().load_file("descriptions/chapterIntro/%s.txt"%(chapter_name))
        reader.getReader().readChapt()
    elif para and not intro:
        reader.getReader().load_file("descriptions/%sparsing/%s.txt"%(chapter_name, file_name))
        reader.getReader().readParag()
    elif not para and not intro:
        reader.getReader().load_file("descriptions/%sparsing/%s.txt"%(chapter_name, file_name))
        reader.getReader().readLine()
    
    #end

def string_parsing1(reader):
    #one just in case I need to make more / create a general one
    locked = False
    fridge = False
    comp = False
    while not (locked and fridge and comp):
        time.sleep(3)
        inp = input(">").lower()
        inp = inp.split()

        #first the general ones
        if "quit" in inp:
            sys.exit()

        #string parsing begins
        elif "pet" in inp and ("cat" in inp or "cats" in inp):
            display_text(reader, "ChapterI", "petCats", True)

        elif "suitcase" in inp and not("look" in inp):
            display_text(reader, "ChapterI", "suitcase")
            locked = True

        elif "fridge" in inp:
            display_text(reader, "ChapterI", "fridge", True)
            fridge = True

        elif "computer" in inp and ("turn" in inp and "off" in inp) and not("look" in inp):
            display_text(reader, "ChapterI", "computerOff", True)
            comp = True

        elif "look" in inp and "computer" in inp:
            display_text(reader, "ChapterI", "computer", True)

        elif "look" in inp and "suitcase" in inp:
            display_text(reader, "ChapterI", "lookSuit", True)

        elif "look" in inp and "keyboard" in inp:
            display_text(reader, "ChapterI", "keyboard", True)

        elif "look" in inp and ("photograph" in inp or "photo" in inp):
            display_text(reader, "ChapterI", "photo", True)


        #a sneeky test
        elif "test" in inp:
            display_text(reader, "ChapterI", "test")

        #input not recognised
        else:
            print("\nI can't do that yet")
    
    print("\nI should leave now") #placeholder



