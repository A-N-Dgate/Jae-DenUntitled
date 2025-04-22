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
        pass

    def __isItemEmpty(self):
        return not self.get_items() #if list = true when list len > 0

    def __str__():
        pass #so this will default right? right??
