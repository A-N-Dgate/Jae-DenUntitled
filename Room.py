from Item import *
from Reader import *

class Room():

    """
    class for instaciating each room in the game.
    """
    def __init__(self, name, desc, items):
        self.name = name
        self.desc = desc
        self.items = items

    def get_name(self): return self.name
    def get_desc(self): return self.desc
    def get_items(self): return self.items

    def remove_item(self, item):
        """
        removes an item from the room's item pool
        """
        if item in self.get_items():
            self.get_items().remove(item)

    def isItemEmpty(self):
        return not self.get_items() #if list = true when list len > 0
    
    def isItemHere(self, itemStr):
        for item in self.get_items():
            if item.get_name() == itemStr:
                return True
        return False
        #clean up?

    def get_item(self, itemStr):
        for item in self.get_items():
            if item.get_name() == itemStr:
                return item



    def __str__(self):
        return "\n %s%s" %(self.get_name(), self.get_desc())
    

#to help with loading the room text
def create_room(player, chaptNo):
    path = "descriptions/Rooms/%s.txt" %(str(chaptNo))
    text = open(path)
    desc = combineText(text)
    #this NEEDS to be cleaned, maybe switch case bc theres only 6 but idk
    match chaptNo:
        case 1:
            name = " Jae's Appartment"
            catWand = Item("cat wand", "used for playing wth my cats.")
            items = [catWand]

    room = Room(name, desc, items)

    player.set_currentRoom(room)
    return player


