from Reader import *
from Character import *
from Item import *
from Room import *
import time
import sys

def create():
    reader = globalReader()
    player = Character()
    chapter = 1
    player = create_room(player, chapter) 
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
        isParagraph = True

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

        elif "look" in inp and ("keyboard" in inp or "piano" in inp):
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
            display_text(reader, "chapterI", obj, isParagraph)

        #separate if branch or whatever you call it
        if inpCounter % 10 == 0:
            time.sleep(3)
            giveHint(reader, comp, locked, fridge)

    time.sleep(3)
    display_text(reader, "ChapterI", "exit")
    time.sleep(3)
    return player

def string_parsing2(reader, player):
    end = False
    #maybe add in booleans for sections of the game being completed?
    #  so that it returns here after each battle?
    while not end:
        obj = None
        time.sleep(3)
        inp = input(">").lower()
        inp = inp.split()
        isParagraph = True

        if "quit" in inp:
            sys.exit()

        elif "inv" in inp:
            print("\n%s" %(player.show_inv()))

        elif "pickup" in inp: 
            player = pickupProcedure(player, inp)

        #^These repeated ones should be in their own method at some point

        elif "look" in inp and "floor" in inp:
            obj = "floor"
            newItem = Item("fluff", "a mysterious piece of white stuffing, a clue maybe?")
            player.get_currentRoom().add_item(newItem)

        elif "look" in inp and "tv" in inp:
            obj = "tv"

        elif "look" in inp and "table" in inp and "clean" not in inp:
            obj = "table"

        elif "look" and ("fluff" in inp or "stuffing" in inp):
            print(showItem(player, "fluff"))
        
        elif "look" in inp:
            print(str(player.get_currentRoom()))

        elif "go" in inp and ("left" in inp or "door" in inp or "wonpil" in inp or "wonpil's" in inp):
            obj = "proceed"
            end = True

        elif "go" in inp: #maybe leaving it non-specific will help not to write a lot of "or"s 
            obj = "cant"

        elif "tv" in inp and "off" in inp:
            obj = "tvOff"

        elif "clean" in inp and ("table" in inp or "floor" in inp):
            obj = "clean"

        else:
            print("\nI can't do that yet")

        #sepreate if branch/chain
        if obj != None:
            display_text(reader, "ChapterII", obj, isParagraph)
    
    return player


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
    isParagraph = True
    time.sleep(3)
    if not comp:
        display_text(reader, "ChapterI", "computerHint", isParagraph)
    elif not locked:
        display_text(reader, "ChapterI", "suitcaseHint", isParagraph)
    elif not fridge:
        display_text(reader, "ChapterI", "fridgeHint", isParagraph)

def removeArticles(inp):
    articles = ["a", "the", "an", "some"]
    returnList = [word for word in inp if word not in articles]
    return returnList
# why isn't "not in" in a fun colour :(



