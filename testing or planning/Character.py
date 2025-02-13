class Character():
    """
    Class used to track what a player has done and where
    they are in the game
    """
    #singleton design pattern????

    def __init__(self):
        self.items = ["", "", "", ""] #fixed amount? I'm not sure becaus eof the suitcase
        self.currentRoom = None
        self.level = 1

    def get_items(self): return self.items
    def get_currentRoom(self): return self.currentRoom
    def get_level(self): return self.level

    def add_item(self, item):
        pass

    def show_inv(self): 
        pass

    def get_item():
        pass

    def __string__():
        return ""
    