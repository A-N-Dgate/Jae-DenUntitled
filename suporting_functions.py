from Reader import *
from Character import *
from Item import *
from Room import *
import time
import sys

def create():
    reader = globalReader()
    player = Character()
    player = create_room(player, 1) #change to generic later? maybe not needed
    return player, reader


def display_text(reader, chapter_name, file_name, para=False, intro=False):
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

    #this needs to be organised better at some point? or don't break it? 

def string_parsing1(reader, player):
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

        elif "look" in inp and ("cat" in inp or "cats" in inp) and (not("pet" in inp or "wand" in inp)):
            display_text(reader, "ChapterI", "lookCats", True)

        elif "look" in inp and "cat" in inp and "wand" in inp:
            if player.get_currentRoom().isItemHere("cat wand"):
                item = player.get_currentRoom().get_item("cat wand")
                print("%s"%(str(item)))

        #now to add in items:
        elif "pickup" in inp and ("cat" in inp and "wand" in inp):
            if player.get_currentRoom().isItemHere("cat wand"):
                item = player.get_currentRoom().get_item("cat wand")
                player = pickup(player, item)

        elif "inv" in inp:
            print("\n%s" %(player.show_inv()))

        elif "look" in inp:
            print(str(player.get_currentRoom()))



        #a sneeky test
        elif "test" in inp:
            display_text(reader, "ChapterI", "test")

        #input not recognised
        else:
            print("\nI can't do that yet")
    
    print("\nI should leave now") #placeholder

def pickup(player, item):
    player.add_item(item)
    item.picked_up()
    player.get_currentRoom().remove_item(item)
    print("\nYou have picked up the %s!" %(str(item)))
    return player



