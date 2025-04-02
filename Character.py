class Character():
    """
    Class used to track what a player has done and where
    they are in the game
    """
    #singleton design pattern???? - maybe not bc it ~might~ be the basis of the devilmalz

    def __init__(self):
        self.items = ["", "", "", ""] #fixed amount? I'm not sure because of the suitcase
        self.itemNo = 0 
        self.currentRoom = None
        self.level = 1

    def get_items(self): return self.items
    def get_currentRoom(self): return self.currentRoom
    def get_level(self): return self.level
    def get_itemNo(self): return self.itemNo

    def itemNo_inc(self): self.itemNo = self.get_itemNo() + 1
    def itemNo_dec(self): self.itemNo = self.get_itemNo() - 1
    #using the set_itemNo(self.get_itemNo() + 1) wasn't working so I thougth I shoudl try this
    #that probably wasn't causing the error but I prefer this method anyway; more abstraction but idk
    #if it is more efficient

    def show_inv(self): 
        if self.get_itemNo() == 0:
            return "You currently don't have any items"
        else:
            itemsStr = "\n".join([str(item) for item in self.get_items()])
            return "The items currently in your inventory are: \n%s" %(itemsStr)

    def add_item(self, item):
        if not self.__isFull():
            #add item
            self.items[self.get_itemNo()] = item
            self.itemNo_inc()
            return "Item added to your inventory!"
        else:
            return "You have no more space in your inventory"


    def __isFull(self):
        return self.get_itemNo() == 4
    

    def __str__(self):
        return "You are currently level %d" %(self.get_level())
    #IF chapt1 THEN
    #   just level
    #ELSE
    #   add in attack, defense and luck stats as well
    #END IF
    