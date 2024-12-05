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
        time.sleep(2)
        inp = input(">")
        inp = inp.split()

        #first the general ones
        if "quit" in inp:
            sys.exit()

        #string parsing begins
        if "pet" in inp and ("cat" in inp or "cats" in inp):
            display_text(reader, "ChapterI", "petCats", True)


        #a sneeky test
        if "test" in inp:
            display_text(reader, "ChapterI", "test")

        #input not recognised
        #else:
            #print("\nYou can't do that yet")



