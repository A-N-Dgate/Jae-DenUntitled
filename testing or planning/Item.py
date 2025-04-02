class Item():
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
        self.pickedUp = False

    def get_name(self): return self.name
    def get_desc(self): return self.desc
    def get_picked(self): return self.pickedUp

    def set_pickedUp(self, a): self.pickedUp = a

    def picked_up(self):
        """
        called when the item is picked up and changes the boolean.
        """
        #don't really need checking here?
        self.set_pickedUp(True)

    def dropped(self):
        """
        called when the item is dropped and changes the boolean.
        """
        self.set_pickedUp(False)

    def show_desc(self):
        """
        returning the description of the item.
        """
        return self.get_desc()

    def __str__(self):
        return self.get_name()

