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
    #unfortunately, I don't know how to clean this one up
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
    inpCounter = 0
    while not (locked and fridge and comp):
        obj = None
        time.sleep(3)
        inp = input(">").lower()
        inp = inp.split()

        inpCounter += 1                                                                                                                                             

        #first the general ones
        if "quit" in inp:
            sys.exit()

        elif "inv" in inp:
            print("\n%s" %(player.show_inv()))

        elif "pickup" in inp: 
            player = pickupProcedure(player, inp)

        #string parsing begins
        elif "pet" in inp and ("cat" in inp or "cats" in inp):
            obj = "PetCats"

        elif "suitcase" in inp and not("look" in inp):
            obj = "suitcase"
            locked = True

        elif "fridge" in inp:
            obj = "fridge"
            fridge = True

        elif "computer" in inp and ("turn" in inp and "off" in inp) and not("look" in inp):
            obj = "computerOff"
            comp = True

        elif "look" in inp and ("computer" in inp or "pc" in inp or "desk" in inp):
            obj = "computer"

        elif "look" in inp and "suitcase" in inp:
            obj = "lookSuit"

        elif "look" in inp and "keyboard" in inp:
            obj = "keyboard"

        elif "look" in inp and ("photograph" in inp or "photo" in inp or "photos" in inp):
            obj = "photo"

        elif "look" in inp and ("cat" in inp or "cats" in inp) and (not("pet" in inp or "wand" in inp)):
            obj = "lookCats"

        elif "look" in inp and "kitchen" in inp:
            obj = "lookKitchen"

        elif "look" in inp and "paper" in inp:
            print(showItem(player, "paper"))

        elif "look" in inp and "cat" in inp and "wand" in inp:
            print(showItem(player, "cat wand"))

        #boolean logic: look needs to be at the end
        elif "look" in inp:
            print(str(player.get_currentRoom()))

        #input not recognised
        else:
            print("\nI can't do that yet")

        #another separate branch added after the tip one
        if obj != None:
            display_text(reader, "ChapterI", obj, True)

        #separate if branch or whatever you call it
        if inpCounter % 10 == 0:
            time.sleep(3)
            giveHint(reader, comp, locked, fridge)

    time.sleep(3)
    display_text(reader, "ChapterI", "exit")
    time.sleep(3)

def string_parsing2(reader, player):
    end = False
    while not end:
        obj = None
        time.sleep(3)
        inp = input(">").lower()
        inp = inp.split()

        if "quit" in inp:
            sys.exit()

        elif "inv" in inp:
            print("\n%s" %(player.show_inv()))

        elif "look" in inp and "floor" in inp:
            obj = "floor"

        elif "look" in inp and ("tv" in inp and "off" in inp):
            obj = "tvOff"

        elif "look" in inp and "tv" in inp:
            obj = "tv"

        elif "look" in inp and "table" in inp:
            obj = "table"
        
        elif "look" in inp:
            print(str(player.get_currentRoom()))

        elif "go" in inp and ("left" in inp or "door" in inp or "wonpil" in inp or "wonpil's" in inp):
            obj = "proceed"
            end = True

        else:
            print("\nI can't do that yet")

        if obj != None:
            display_text(reader, "ChapterII", obj, True)


def pickupProcedure(player, inp):
    inp = removeArticles(inp)
    itemStr = " ".join(inp[1:])
    if player.get_currentRoom().isItemHere(itemStr):
        item = player.get_currentRoom().get_item(itemStr)
        player = pickup(player, item)
    else:
        print("\nYou cannot pickup %s"%(itemStr))

    return player

def showItem(player, itemName):
    if player.get_currentRoom().isItemHere(itemName):
        item = player.get_currentRoom().get_item(itemName)
        return "\n%s"%(item.show_desc())
    else:
        return "\nIt is now in your inventory"

def pickup(player, item):
    player.add_item(item)
    item.picked_up()
    player.get_currentRoom().remove_item(item)
    print("\nYou have picked up the %s!" %(str(item)))
    return player

def giveHint(reader, comp, locked, fridge):
    time.sleep(3)
    if not comp:
        display_text(reader, "ChapterI", "computerHint", True)
    elif not locked:
        display_text(reader, "ChapterI", "suitcaseHint", True)
    elif not fridge:
        display_text(reader, "ChapterI", "fridgeHint", True)

def removeArticles(inp):
    articles = ["a", "the", "an", "some"]
    returnList = [word for word in inp if word not in articles]
    return returnList
# why isn't "not in" in a fun colour :(



